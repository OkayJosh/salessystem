from rest_framework import viewsets

from .serializers import LeadSerializer, PurchaseSerializer

from .models import Lead, Purchase

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
