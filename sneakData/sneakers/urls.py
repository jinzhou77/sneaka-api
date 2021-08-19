from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sneakers', SneakersViewSet, basename='sneakers')
router.register(r'trades', SneakersTradingViewSet, basename='trades')
router.register(r'ebaytrades', SneakerEbayTradingViewSet, basename='ebaytrades')
urlpatterns = router.urls
