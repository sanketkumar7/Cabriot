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

class DailyDisplayAssignment(models.Model):
    SECTION_CHOICES = [
        ('MenuItem', 'Menu Item'),
        ('Ingredient', 'Ingredient'),
        ('Bread', 'Bread')
    ]

    date = models.DateField()
    meal_period = models.CharField(
        max_length=20,
        choices=[('Breakfast/Lunch', 'Breakfast/Lunch'), ('Dinner', 'Dinner')]
    )
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    item_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_type = models.CharField(
        max_length=10,
        choices=[('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Numbers', 'Numbers')]
    )

    def __str__(self):
        return f"{self.date} - {self.meal_period} - {self.section} - {self.item_name}"

class MealTime(models.Model):
    breakfast_lunch_start_time=models.TimeField(null=True,blank=True)
    breakfast_lunch_end_time=models.TimeField(null=True,blank=True)
    dinner_start_time=models.TimeField(null=True,blank=True)
    dinner_end_time=models.TimeField(null=True,blank=True)