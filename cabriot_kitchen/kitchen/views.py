from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import MenuItem, Ingredient, Bread

def get_items(request, section):
    print('I am here...')
    items = []
    if section == 'MenuItem':
        items = list(MenuItem.objects.values('id', 'name'))
    elif section == 'Ingredient':
        items = list(Ingredient.objects.values('id', 'name'))
    elif section == 'Bread':
        items = list(Bread.objects.values('id', 'name'))
    return JsonResponse({'items': items})
