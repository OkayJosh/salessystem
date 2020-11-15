import pytest
import datetime
from django.utils.timezone import now
from rest_framework import serializers
from django.test import TestCase, override_settings
from phonenumber_field import phonenumber

from .models import Lead, Purchase
from .serializers import LeadSerializer, PurchaseSerializer

from rest_framework.viewsets import ModelViewSet
from collections import OrderedDict
from functools import wraps




from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.test import APIRequestFactory

from .views import LeadViewSet
factory = APIRequestFactory()

class LeadModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Lead.objects.create( name ='Geniva', phone_number='+418168518511', email='geniva@geniva.com')

    def test_name_label(self):
        lead = Lead.objects.get(id=1)
        field_label = lead._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_phone_number_label(self):
        lead=Lead.objects.get(id=1)
        field_label = lead._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_name_max_length(self):
        lead = Lead.objects.get(id=1)
        max_length = lead._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_first_name_comma_email(self):
        lead = Lead.objects.get(id=1)
        expected_object_name = f'{lead.name}, {lead.email}'
        self.assertEqual(expected_object_name, str(lead))

class PurchaseModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Purchase.objects.create( name ='Geniva', number='11', date=now())

    def test_name_label(self):
        purchase = Purchase.objects.get(id=1)
        field_label = purchase._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_number_label(self):
        purchase = Purchase.objects.get(id=1)
        field_label = purchase._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')

    def test_name_max_length(self):
        purchase = Purchase.objects.get(id=1)
        max_length = purchase._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_first_name_comma_date(self):
        purchase = Purchase.objects.get(id=1)
        expected_object_name = f'{purchase.name}, {purchase.date}'
        self.assertEqual(expected_object_name, str(purchase))

# Serializer Tests
class LeadSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.lead_attributes = {
            'name': 'geniva',
            'phone_number': '+418168518511',
            'email': 'joshua@geneva.com'
        }

        self.serializer_data = {
            'name': 'geniva',
            'phone_number': '+418168518511',
            'email': 'joshua@geneva.com'
        }

        self.lead = Lead.objects.create(**self.lead_attributes)
        self.serializer = LeadSerializer(instance=self.lead)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'phone_number', 'email']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.lead_attributes['name'])

    def test_phone_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['phone_number'], self.lead_attributes['phone_number'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.lead_attributes['email'])


class PurchaseSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.purchase_attributes = {
            'name': 'geniva',
            'number': int('511'),
            'date': '2020-11-15'
        }

        self.serializer_data = {
            'name': 'geniva',
            'phone_number': '511',
            'date': '2020-11-15'
        }

        self.purchase = Purchase.objects.create(**self.purchase_attributes)
        self.serializer = PurchaseSerializer(instance=self.purchase)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'number', 'date']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.purchase_attributes['name'])

    def test_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['number'], self.purchase_attributes['number'])

    def test_date_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['date'], self.purchase_attributes['date'])


