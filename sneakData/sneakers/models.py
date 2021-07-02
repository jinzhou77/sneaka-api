from django.db import models
import uuid

# Create your models here.

class Detail(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255, null=False)
    brandname = models.CharField(max_length=255, null=False)
    stylename = models.CharField(max_length=255, null=True)
    imagepath = models.CharField(max_length=255, null=True)
    retailprice = models.DecimalField(null=True, default=0.0, decimal_places=2, max_digits=10)
    numberofsale = models.IntegerField(default=0)
    averagesaleprice = models.DecimalField(null=True, default=0.0, decimal_places=2, max_digits=10)
    stylecode = models.CharField(max_length=255, null=True)
    colorway = models.CharField(max_length=255, null=True)
    ticker = models.CharField(max_length=255, null=True)
    releasedate = models.DateTimeField(auto_now=False, null=True)
