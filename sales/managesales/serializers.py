from rest_framework import serializers

from .models import Lead, Purchase

class LeadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lead
        fields = ['name', 'phone_number', 'email']

class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = ['name', 'number', 'date']