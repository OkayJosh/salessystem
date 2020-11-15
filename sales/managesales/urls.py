from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, PurchaseViewSet


router = DefaultRouter()
router.register('leads', LeadViewSet, basename='sales-leads')
router.register('purchase', PurchaseViewSet, basename='sales-purchase')

urlpatterns = [
    
] + router.urls