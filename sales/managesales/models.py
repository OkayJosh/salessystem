from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField("phone number")
    email = models.EmailField(help_text="Enter your Email here")

    def __str__(self):
        return f'{self.name}, {self.email}'

class Purchase( models.Model):
    name = models.CharField(max_length=200, help_text="Enter the name of the purchased Item")
    number = models.PositiveIntegerField(help_text="Enter the quantity purchased")
    date = models.DateField()

    def __str__(self):
        return f'{self.name}, {self.date}'