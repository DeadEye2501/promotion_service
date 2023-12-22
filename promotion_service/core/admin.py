from django.contrib import admin
from .models import *


@admin.register(StockPrice)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
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
