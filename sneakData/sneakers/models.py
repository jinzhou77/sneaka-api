from django.db import models
import uuid

# Create your models here.

class Detail(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    shoe = models.CharField(max_length=255, null=True)
    colorway = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255, null=False)
    thumb_url = models.CharField(max_length=255, null=False)
    release_date = models.CharField(max_length=255, null=True)
    below_retail = models.BooleanField() 
    retail_price = models.DecimalField(null=True, decimal_places=2, max_digits=10) 
    style_id = models.CharField(max_length=255, null=True)
    ticker_symbol = models.CharField(max_length=255, null=False)
    url_key = models.CharField(max_length=255, null=False)    
    title = models.CharField(max_length=255, null=False) 
    market_annual_high = models.DecimalField(null=True, decimal_places=2, max_digits=10) 
    market_annual_low = models.DecimalField(null=True, decimal_places=2, max_digits=10) 
    market_sales_last_72hours = models.IntegerField()
    market_lowest_ask = models.DecimalField(null=True, decimal_places=2, max_digits=10) 
    market_lowest_ask_size = models.CharField(max_length=255, null=True) 
    market_highest_bid = models.DecimalField(null=True, decimal_places=2, max_digits=10) 
    market_highest_bid_size = models.CharField(max_length=255, null=True) 

class Stockx(models.Model):
    analyze_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sneaker = models.ForeignKey(Detail, on_delete=models.CASCADE)
    analyze_target_date = models.CharField(max_length=255, null=False)
    size = models.CharField(max_length=255, null=False)
    average_price = models.CharField(max_length=255, null=True)
    high_price = models.CharField(max_length=255, null=True)
    low_price = models.CharField(max_length=255, null=True)
    number_of_trades = models.IntegerField()
    publish_date = models.CharField(max_length=255, null=False)

class EbayTrades(models.Model):
    ebay_trade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ebay_trade_name = models.CharField(max_length=255, null=False)
    ebay_trade_url = models.CharField(max_length=255, null=False)
    seller =  models.CharField(max_length=255, null=False)
    sold_price =  models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)
    ship_fee =  models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)
    size = models.DecimalField(null=False, default=0.0, decimal_places=2, max_digits=10)
    sold_date = models.DateTimeField(auto_now=False, null=False)
    condition = models.CharField(max_length=255, null=False)
