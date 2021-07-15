from rest_framework import serializers
from .models import *


class SneakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('product_id', 'url','brand_name','style_name','image_path', 'retail_price', 'number_of_sale', 'average_sale_price', 'style_code', 'colorway', 'ticker', 'release_date')

class SneakerTradingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trades
        fields = ('trade_id', 'trade_name', 'ticker', 'trade_date_time', 'trade_size', 'trade_price')
