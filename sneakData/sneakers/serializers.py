from rest_framework import serializers
from .models import *


class SneakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('product_id', 'url', 'brand_name', 'model_name', 'style_name', 'number_sales_72_hours', 'ticker', 'image_path', 'release_date', 'retail_price', 'style_code', 'colorway', 'number_sales_12_months', 'price_premium', 'average_sales_price')

class SneakerTradingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trades
        fields = ('trade_id', 'trade_name', 'ticker', 'trade_date_time', 'trade_size', 'trade_price')

class SneakerEbayTradingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EbayTrades
        fields = ('ebay_trade_id', 'ebay_trade_name', 'ebay_trade_url', 'seller', 'sold_price', 'ship_fee', 'size', 'sold_date', 'condition')

