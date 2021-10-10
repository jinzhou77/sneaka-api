from __future__ import unicode_literals

from django.db.models.aggregates import Count, Sum

from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import date
from django.db.models import Min, Max
# Create your views here.


class SneakersViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerModelSerializer

    def get_queryset(self):
        queryset = Detail.objects.all()

        if self.request.query_params.get('product_id') is not None:
            return queryset.filter(product_id=self.request.query_params.get('product_id'))
        if self.request.query_params.get('brand') is not None:
            return queryset.filter(brand=self.request.query_params.get('brand'))
        if self.request.query_params.get("popularity") is not None and self.request.query_params.get("popularity") == 'true':
            return queryset.order_by('-market_sales_last_72hours')
        if self.request.query_params.get("recent_release") is not None and self.request.query_params.get("recent_release") == 'true':
            today = date.today()
            queryset = queryset.filter(release_date__isnull=False)
            queryset = queryset.filter(release_date__lt=today)
            return queryset.order_by('-release_date')

        return queryset

    def create(self, request):
        product_id = request.data.get('product_id')
        brand = request.data.get('brand')
        category = request.data.get('category')
        shoe = request.data.get('shoe')
        colorway = request.data.get('colorway')
        gender = request.data.get('gender')
        image_url = request.data.get('image_url')
        thumb_url = request.data.get('thumb_url')
        release_date = request.data.get('release_date')
        below_retail = request.data.get('below_retail')
        retail_price = request.data.get('retail_price')
        style_id = request.data.get('style_id')
        ticker_symbol = request.data.get('ticker_symbol')
        url_key = request.data.get('url_key')
        title = request.data.get('title')
        market_annual_high = request.data.get('market_annual_high')
        market_annual_low = request.data.get('market_annual_low')
        market_sales_last_72hours = request.data.get(
            'market_sales_last_72hours')
        market_lowest_ask = request.data.get('market_lowest_ask')
        market_lowest_ask_size = request.data.get('market_lowest_ask_size')
        market_highest_bid = request.data.get('market_highest_bid')
        market_highest_bid_size = request.data.get(
            'marketHighmarket_highest_bid_sizeestBidSize')

        instance = Detail(
            product_id=product_id,
            brand=brand,
            category=category,
            shoe=shoe,
            colorway=colorway,
            gender=gender,
            image_url=image_url,
            thumb_url=thumb_url,
            release_date=release_date,
            below_retail=below_retail,
            retail_price=retail_price,
            style_id=style_id,
            ticker_symbol=ticker_symbol,
            url_key=url_key,
            title=title,
            market_annual_high=market_annual_high,
            market_annual_low=market_annual_low,
            market_sales_last_72hours=market_sales_last_72hours,
            market_lowest_ask=market_lowest_ask,
            market_lowest_ask_size=market_lowest_ask_size,
            market_highest_bid=market_highest_bid,
            market_highest_bid_size=market_highest_bid_size
        )
        instance.save()
        return Response({
            'product_id': product_id,
            'brand': brand,
            'category': category,
            'shoe': shoe,
            'colorway': colorway,
            'gender': gender,
            'image_url': image_url,
            'thumb_url': thumb_url,
            'release_date': release_date,
            'below_retail': below_retail,
            'retail_price': retail_price,
            'style_id': style_id,
            'ticker_symbol': ticker_symbol,
            'url_key': url_key,
            'title': title,
            'market_annual_high': market_annual_high,
            'market_annual_low': market_annual_low,
            'market_sales_last_72hours': market_sales_last_72hours,
            'market_lowest_ask': market_lowest_ask,
            'market_lowest_ask_size': market_lowest_ask_size,
            'market_highest_bid': market_highest_bid,
            'market_highest_bid_size': market_highest_bid_size
        }, status=status.HTTP_201_CREATED)
class MonthlyAnalyzeViewSet(viewsets.ModelViewSet):
    serializer_class = MonthlyAnalyzeModelSerializer

    def get_queryset(self):
        queryset = Analyze.objects.filter(analyze_target_date__range=["2021-09-04", "2021-10-30"])
        if self.request.query_params.get('size') is not None:
            queryset = queryset.filter(size=self.request.query_params.get('size'))
        queryset = queryset.values('platform').annotate(monthly_low=Min('low_price'), monthly_high=Max('high_price'), monthly_trades=Sum('number_of_trades'))
        return queryset
    
class AnalyzeViewSet(viewsets.ModelViewSet):
    serializer_class = AnalyzeModelSerializer

    def get_queryset(self):
        queryset = Analyze.objects.all()
        queryset = queryset.order_by("analyze_target_date")
        queryset = queryset.filter(analyze_target_date__range=["2021-09-04", "2021-10-30"])
        if self.request.query_params.get('size') is not None:
            queryset = queryset.filter(size=self.request.query_params.get('size'))
        return queryset

    def create(self, request):
        sneaker_id = request.data.get("product_id")
        analyze_target_date = request.data.get('analyze_target_date')
        size = request.data.get('size')
        average_price = request.data.get('average_price')
        high_price = request.data.get('high_price')
        low_price = request.data.get('low_price')
        number_of_trades = request.data.get('number_of_trades')
        publish_date = request.data.get('publish_date')
        platform = request.data.get('platform')
        
        instance = Analyze(sneaker=Detail.objects.get(product_id=sneaker_id), analyze_target_date=analyze_target_date, size=size,
                                 average_price=average_price, high_price=high_price, low_price=low_price, number_of_trades=number_of_trades, publish_date=publish_date, platform=platform)
        instance.save()
        return Response({
            'sneaker_id': sneaker_id,
            'analyze_target_date': analyze_target_date,
            'size': size,
            'average_price': average_price,
            'high_price': high_price,
            'low_price': low_price,
            'number_of_trades': number_of_trades,
            'publish_date': publish_date,
            'platform': platform
        }, status=status.HTTP_201_CREATED)


class SneakerEbayTradingViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerEbayTradingModelSerializer

    def get_queryset(self):
        queryset = EbayTrades.objects.all()
        return queryset

    def create(self, request):
        ebay_trade_name = request.data.get('ebay_trade_name')
        ebay_trade_url = request.data.get('ebay_trade_url')
        seller = request.data.get("seller")
        sold_price = request.data.get("sold_price")
        ship_fee = request.data.get("ship_fee")
        size = request.data.get("size")
        sold_date = request.data.get("sold_date")
        condition = request.data.get("condition")
        instance = EbayTrades(ebay_trade_name=ebay_trade_name, ebay_trade_url=ebay_trade_url, seller=seller,
                              sold_price=sold_price, ship_fee=ship_fee, size=size, sold_date=sold_date, condition=condition)
        instance.save()
        return Response({
            'ebay_trade_name': ebay_trade_name,
            'ebay_trade_url': ebay_trade_url,
            'seller': seller,
            'sold_price': sold_price,
            'ship_fee': ship_fee,
            'size': size,
            'sold_data': sold_date,
            'condition': condition
        })
