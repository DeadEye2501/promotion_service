from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        return User.objects.create(**validated_data)


class GetPromotionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = (
            'id',
            'ticker',
            'volume',
            'volume_weighted',
            'open_price',
            'close_price',
            'high_price',
            'low_price',
            'timestamp',
            'trades_count'
        )


class PutPromotionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = (
            'ticker',
            'volume',
            'volume_weighted',
            'open_price',
            'close_price',
            'high_price',
            'low_price',
            'timestamp',
            'trades_count'
        )
        extra_kwargs = {
            'ticker': {'required': False},
            'volume': {'required': False},
            'volume_weighted': {'required': False},
            'open_price': {'required': False},
            'close_price': {'required': False},
            'high_price': {'required': False},
            'low_price': {'required': False},
            'timestamp': {'required': False},
            'trades_count': {'required': False},
        }
