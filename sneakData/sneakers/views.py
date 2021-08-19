from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from datetime import date
# Create your views here.
class SneakersViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerModelSerializer
        
    def get_queryset(self):
        queryset = Detail.objects.all()
        
        if self.request.query_params.get('product_id') is not None:
            return queryset.filter(product_id=self.request.query_params.get('product_id'))
        if self.request.query_params.get('brand') is not None:
            return queryset.filter(brand_name=self.request.query_params.get('brand').replace("-", " "))
        if self.request.query_params.get("popularity") is not None and self.request.query_params.get("popularity")=='true':
            return queryset.order_by('-number_sales_72_hours')[:4]
        if self.request.query_params.get("recent_release") is not None and self.request.query_params.get("recent_release")=='true':
            today = date.today()
            queryset = queryset.filter(release_date__isnull=False)
            queryset = queryset.filter(release_date__lt=today)
            return queryset.order_by('-release_date')[:4]
    
        return queryset
    
    def create(self, request):
        url = request.data.get('url')
        brand_name = request.data.get('brand_name')
        model_name = request.data.get('model_name')
        style_name = request.data.get('style_name')
        number_sales_72_hours =request.data.get('number_sales_72_hours')
        ticker =  request.data.get('ticker')
        image_path = request.data.get('image_path')
        release_date =request.data.get('release_date')
        retail_price = request.data.get('retail_price')
        style_code = request.data.get('style_code') 
        colorway = request.data.get('colorway')
        number_sales_12_months = request.data.get('number_sales_12_months')
        price_premium = request.data.get('price_premium')
        average_sales_price = request.data.get('average_sales_price')
        
        instance = Detail(
            url=url, 
            brand_name=brand_name,
            model_name=model_name, 
            style_name=style_name, 
            number_sales_72_hours=number_sales_72_hours, 
            ticker=ticker, 
            image_path=image_path, 
            release_date=release_date, 
            retail_price=retail_price, 
            style_code=style_code, 
            colorway=colorway, 
            number_sales_12_months=number_sales_12_months, 
            price_premium=price_premium, 
            average_sales_price=average_sales_price
            )
        instance.save()
        return Response({
            'url':url, 
            'brand_name':brand_name, 
            'model_name':model_name,
            'style_name':style_name, 
            'number_sales_72_hours':number_sales_72_hours, 
            'ticker':ticker, 
            'image_path':image_path, 
            'release_date':release_date, 
            'retail_price':retail_price, 
            'style_code':style_code, 
            'colorway':colorway, 
            'number_sales_12_months':number_sales_12_months, 
            'price_premium':price_premium, 
            'average_sales_price':average_sales_price
            }, status=status.HTTP_201_CREATED)

class SneakersTradingViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerTradingModelSerializer

    def get_queryset(self):
        queryset = Trades.objects.all()
        return queryset

    def create(self, request):
        trade_name = request.data.get('trade_name')
        ticker = request.data.get('ticker')
        trade_date_time = request.data.get('trade_date_time')
        trade_size = request.data.get('trade_size')
        trade_price = request.data.get('trade_price')
        instance = Trades(trade_name=trade_name, ticker=ticker, trade_date_time=trade_date_time, trade_size=trade_size, trade_price=trade_price)
        instance.save()
        return Response({
            'trade_name': trade_name,
            'ticker': ticker,
            'trade_date_time': trade_date_time,
            'trade_size': trade_size,
            'trade_price': trade_price
        })

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
        instance = EbayTrades(ebay_trade_name=ebay_trade_name, ebay_trade_url=ebay_trade_url, seller=seller, sold_price=sold_price, ship_fee=ship_fee, size=size, sold_date=sold_date, condition=condition)
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