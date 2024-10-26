from django.shortcuts import render
from datetime import datetime 

from django.http import JsonResponse
from .models import MenuItem, Ingredient, Bread,DailyDisplayAssignment,MealTime

def get_items(request, section):
    items = []
    if section == 'MenuItem':
        items = list(MenuItem.objects.values('id', 'name'))
    elif section == 'Ingredient':
        items = list(Ingredient.objects.values('id', 'name'))
    elif section == 'Bread':
        items = list(Bread.objects.values('id', 'name'))
    return JsonResponse({'items': items})

def display_main_items_view(request):
    foods={}
    current_datetime=datetime.now()
    current_time=current_datetime.time()
    date=current_datetime.date()
    instance=MealTime.objects.first()
    breakfast_lunch_start = instance.breakfast_lunch_start_time
    breakfast_lunch_end = instance.breakfast_lunch_end_time
    dinner_start = instance.dinner_start_time
    dinner_end = instance.dinner_end_time

    # Compare current time with meal times
    if breakfast_lunch_start <= current_time and current_time <= breakfast_lunch_end:
        meal_status = "Breakfast/Lunch"
    elif dinner_start <= current_time and current_time <= dinner_end:
        meal_status = "Dinner"
    else:
        meal_status = "No meal time currently."
    daily_main=DailyDisplayAssignment.objects.filter(date=date,meal_period=meal_status,section='MenuItem').values()
    print(daily_main)
    if (daily_main):
        for each in daily_main:
            item_id = each['item_name']  # Assuming 'item_name' holds the ID of MenuItem
            menu_item = MenuItem.objects.get(id=item_id)
            foods[item_id] = {
                'item':menu_item,
                'quantity': each['quantity'],
                'quantity_type': each['quantity_type']
            }
    context={
        'foods':foods,
        'meal':meal_status,
        'section':'MAIN',
    }
    return render(request,'kitchen/menu_items.html',context)
def display_vegetables_view(request):
    foods={}
    current_datetime=datetime.now()
    current_time=current_datetime.time()
    date=current_datetime.date()
    instance=MealTime.objects.first()
    breakfast_lunch_start = instance.breakfast_lunch_start_time
    breakfast_lunch_end = instance.breakfast_lunch_end_time
    dinner_start = instance.dinner_start_time
    dinner_end = instance.dinner_end_time

    # Compare current time with meal times
    if breakfast_lunch_start <= current_time and current_time <= breakfast_lunch_end:
        meal_status = "Breakfast/Lunch"
    elif dinner_start <= current_time and current_time <= dinner_end:
        meal_status = "Dinner"
    else:
        meal_status = "No meal time currently."
    daily_main=DailyDisplayAssignment.objects.filter(date=date,meal_period=meal_status,section='Ingredient').values()
    print(daily_main)
    if (daily_main):
        for each in daily_main:
            item_id = each['item_name']  # Assuming 'item_name' holds the ID of MenuItem
            menu_item = Ingredient.objects.get(id=item_id)
            foods[item_id] = {
                'item': menu_item,
                'quantity': each['quantity'],
                'quantity_type': each['quantity_type']
            }
    context={
        'foods':foods,
        'meal':meal_status,
    }
    return render(request,'kitchen/vegetable.html',context)

def display_bread_view(request):
    foods={}
    current_datetime=datetime.now()
    current_time=current_datetime.time()
    date=current_datetime.date()
    instance=MealTime.objects.first()
    breakfast_lunch_start = instance.breakfast_lunch_start_time
    breakfast_lunch_end = instance.breakfast_lunch_end_time
    dinner_start = instance.dinner_start_time
    dinner_end = instance.dinner_end_time

    # Compare current time with meal times
    if breakfast_lunch_start <= current_time and current_time <= breakfast_lunch_end:
        meal_status = "Breakfast/Lunch"
    elif dinner_start <= current_time and current_time <= dinner_end:
        meal_status = "Dinner"
    else:
        meal_status = "No meal time currently."
    daily_main=DailyDisplayAssignment.objects.filter(date=date,meal_period=meal_status,section='Bread').values()
    print(daily_main)
    if (daily_main):
        for each in daily_main:
            item_id = each['item_name']  # Assuming 'item_name' holds the ID of MenuItem
            menu_item = Bread.objects.get(id=item_id)
            foods[item_id] = {
                'item': menu_item,
                'quantity': each['quantity'],
                'quantity_type': each['quantity_type']
            }
    context={
        'foods':foods,
        'meal':meal_status,

    }
    return render(request,'kitchen/bread.html',context)