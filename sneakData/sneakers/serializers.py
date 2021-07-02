from rest_framework import serializers
from .models import *


class SneakerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('url','brandname','stylename','imagepath', 'retailprice', 'numberofsale', 'averagesaleprice', 'stylecode', 'colorway', 'ticker', 'releasedate')
