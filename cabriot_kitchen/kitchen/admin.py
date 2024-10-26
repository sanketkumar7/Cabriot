from django.contrib import admin
from .models import MenuItem,Ingredient,Bread
# Register your models here.
class Menu(admin.ModelAdmin):
    list_display=['title','name','image']
admin.site.register(MenuItem,Menu)

class Ingre(admin.ModelAdmin):
    list_display=['title','name','image']
admin.site.register(Ingredient,Ingre)

class bread(admin.ModelAdmin):
    list_display=['title','name','image']
admin.site.register(Bread,bread)
