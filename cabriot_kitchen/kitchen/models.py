from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='MenuItem/')

class Ingredient(models.Model):
    title=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='Ingredient/')

class Bread(models.Model):
    title=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='Bread/')