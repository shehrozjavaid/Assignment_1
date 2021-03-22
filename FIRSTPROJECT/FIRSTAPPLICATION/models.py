from django.db import models

# Create your models here.
class Name(models.Model):
    Name_text=models.CharField(max_length=200)
    def __str__(self):
        return self.Name_text

class Contact(models.Model):
    phone_number=models.CharField(max_length=200)
    def __str__(self):
        return self.phone_number

class Address(models.Model):
    Address=models.CharField(max_length=200)
    def __str__(self):
        return self.Address

class ID(models.Model):
    ID_user=models.CharField(max_length=200)
    def __str__(self):
        return self.ID_user
