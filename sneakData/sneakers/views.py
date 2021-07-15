from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.response import Response

# Create your views here.
class SneakersViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerModelSerializer

    def get_queryset(self):
        queryset = Detail.objects.filter(number_of_sale__gt=0)
        if self.request.query_params.get('brand') is not None:
            return queryset.filter(brand_name=self.request.query_params.get('brand'))
        return queryset
    
    def create(self, request):
        url = request.data.get('url')
<<<<<<< HEAD
        brand_name = request.data.get('brand_name')
        style_name = request.data.get('style_name')
        image_path = request.data.get('image_path')
        retail_price = request.data.get('retail_price')        
        number_of_sale = request.data.get('number_of_sale')
        averge_sale_price = request.data.get('average_sale_price')
        style_code = request.data.get('style_code')
        colorway = request.data.get('coloway')
=======
        brandName = request.data.get('brandname')
        styleName = request.data.get('stylename')
        imagePath = request.data.get('imagepath')
        retailPrice = request.data.get('retailprice')        
        numberOfSale = request.data.get('numberofsale')
        averageSalePrice = request.data.get('averagesaleprice')
        styleCode = request.data.get('stylecode')
        colorWay = request.data.get('colorway')
>>>>>>> 155297f589b3d06caf0bfaee6d2913c806cface5
        ticker = request.data.get('ticker')
        release_date = request.data.get('release_date')
        instance = Detail(url=url, brand_name=brand_name, style_name=style_name, image_path=image_path, retail_price = retail_price, number_of_sale = number_of_sale, averge_sale_price=averge_sale_price, style_code=style_code, colorway=colorway, ticker=ticker, release_date=release_date)
        instance.save()
        return Response({
            'url':  url, 
            'brand_name': brand_name, 
            'style_name': style_name,
            'image_path': image_path,
            'retail_price':  retail_price,
            'number_of_sale' : number_of_sale,
            'averge_sale_price': averge_sale_price,
            'style_code': style_code,
            'colorway': colorway,
            'ticker': ticker,
            'release_date': release_date,
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