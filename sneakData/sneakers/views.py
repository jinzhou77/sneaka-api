from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.response import Response

# Create your views here.
class SneakersViewSet(viewsets.ModelViewSet):
    serializer_class = SneakerModelSerializer

    def get_queryset(self):
        queryset = Detail.objects.filter(numberofsale__gt=0)
        if self.request.query_params.get('brand') is not None:
            return queryset.filter(brandname=self.request.query_params.get('brand'))
        return queryset
    
    def create(self, request):
        url = request.data.get('url')
        brandName = request.data.get('brandname')
        styleName = request.data.get('stylename')
        imagePath = request.data.get('imagepath')
        retailPrice = request.data.get('retailprice')        
        numberOfSale = request.data.get('numberofsale')
        averageSalePrice = request.data.get('averagesaleprice')
        styleCode = request.data.get('stylecode')
        colorWay = request.data.get('colorway')
        ticker = request.data.get('ticker')
        releaseDate = request.data.get('releasedate')
        instance = Detail(url=url, brandname=brandName, stylename=styleName, imagepath=imagePath, retailprice = retailPrice, numberofsale = numberOfSale, averagesaleprice=averageSalePrice, stylecode=styleCode, colorway=colorWay, ticker=ticker, releasedate=releaseDate)
        instance.save()
        return Response({
            'url': request.data.get('url') , 
            'brandName': request.data.get('stylename'), 
            'styleName': request.data.get('stylename'),
            'imagePath': request.data.get('imagepath'),
            'retailPrice':  request.data.get('retailprice'),
            'numberofsale' : request.data.get('numberofsale'),
            'averageSalePrice': request.data.get('averagesaleprice'),
            'styleCode': request.data.get('stylecode'),
            'colorWay': request.data.get('coloway'),
            'ticker':request.data.get('ticker'),
            'releaseDate': request.data.get('releasedate')
            }, status=status.HTTP_201_CREATED)