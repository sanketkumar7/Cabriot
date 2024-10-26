from django.contrib import admin
from .models import MenuItem,Ingredient,Bread,DailyDisplayAssignment
from .forms import DailyDisplayAssignmentForm
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


class daily_display(admin.ModelAdmin):
    form = DailyDisplayAssignmentForm
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js',
            'admin/daily_display_assignment.js'
            )
        
    list_display=['date','meal_period','section','item_name','quantity','quantity_type']
admin.site.register(DailyDisplayAssignment,daily_display)