from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from drf_spectacular.utils import extend_schema
from .utils import *
from .serializers import *


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class GetStockDataApiView(APIView):
    @staticmethod
    def get(request, date_from, date_to):
        data = get_values(date_from, date_to)
        serializer = GetPromotionDataSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(request=PutPromotionDataSerializer)
class UpdateStockDataApiView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            stock_price = StockPrice.objects.get(pk=pk)
            serializer = PutPromotionDataSerializer(instance=stock_price, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': 'This StockPrice not found'}, status=status.HTTP_400_BAD_REQUEST)
