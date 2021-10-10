from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sneakers', SneakersViewSet, basename='sneakers')
router.register(r'analyze', AnalyzeViewSet, basename='trades')
router.register(r'monthly', MonthlyAnalyzeViewSet, basename='monthly')
router.register(r'ebaytrades', SneakerEbayTradingViewSet, basename='ebaytrades')
urlpatterns = router.urls
