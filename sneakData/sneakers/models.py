from django.db import models
import uuid

# Create your models here.

class Detail(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255, null=False)
    brand_name = models.CharField(max_length=255, null=False)
    style_name = models.CharField(max_length=255, null=True)
    image_path = models.CharField(max_length=255, null=True)
    retail_price = models.DecimalField(null=True, default=0.0, decimal_places=2, max_digits=10)
    number_of_sale = models.IntegerField(default=0)
    averge_sale_price = models.DecimalField(null=True, default=0.0, decimal_places=2, max_digits=10)
    style_code = models.CharField(max_length=255, null=True)
    colorway = models.CharField(max_length=255, null=True)
    ticker = models.CharField(max_length=255, null=True)
    release_date = models.DateTimeField(auto_now=False, null=True)

class Trades(models.Model):
    trade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trade_name = models.CharField(max_length=255, null=False)
    ticker = models.CharField(max_length=255, null=False)
    trade_date_time = models.DateTimeField(auto_now=False, null=False)
    trade_size = models.CharField(max_length=255, null=False)
    trade_price = models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)