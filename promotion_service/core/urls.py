from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='registration'),
    path('stock_data/<str:date_from>/<str:date_to>/', GetStockDataApiView.as_view(), name='get_stock_data'),
    path('stock_data/<int:pk>/', UpdateStockDataApiView.as_view(), name='update_stock_data'),
]
