from django.db import models


class StockPrice(models.Model):
    class Meta:
        verbose_name = 'Информация о стоимости акции'
        verbose_name_plural = 'Информация о стоимости акций'

    ticker = models.CharField(max_length=10, verbose_name='Тикер')
    volume = models.IntegerField(verbose_name='Объем')
    volume_weighted = models.FloatField(verbose_name='Взвешенный объем')
    open_price = models.FloatField(verbose_name='Цена открытия')
    close_price = models.FloatField(verbose_name='Цена закрытия')
    high_price = models.FloatField(verbose_name='Максимальная цена')
    low_price = models.FloatField(verbose_name='Минимальная цена')
    timestamp = models.DateTimeField(verbose_name='Временная метка')
    trades_count = models.IntegerField(verbose_name='Количество сделок')

    def __str__(self):
        return f'{self.ticker}: {self.timestamp}'
