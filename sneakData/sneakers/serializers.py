from rest_framework import serializers
from .models import *


class SneakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('product_id', 'brand', 'category', 'shoe', 'colorway', 'gender', 'image_url', 'thumb_url', 'release_date', 'below_retail', 'retail_price', 'style_id', 'ticker_symbol', 'url_key', 'title', 'market_annual_high','market_annual_low','market_sales_last_72hours','market_lowest_ask','market_lowest_ask_size','market_highest_bid', 'market_highest_bid_size')

class AnalyzeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyze
        fields = ('analyze_id', 'sneaker', 'analyze_target_date', 'size', 'average_price', 'high_price', 'low_price', 'number_of_trades', 'publish_date', 'platform')

class MonthlyAnalyzeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyAnalyze
        fields = ('platform', 'monthly_high', 'monthly_low', 'monthly_trades')
        
class SneakerEbayTradingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EbayTrades
        fields = ('ebay_trade_id', 'ebay_trade_name', 'ebay_trade_url', 'seller', 'sold_price', 'ship_fee', 'size', 'sold_date', 'condition')

