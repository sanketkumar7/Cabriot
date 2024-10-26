from django.urls import path
from . import views
urlpatterns=[
    path('get_items/<str:section>/', views.get_items, name='get_items'),
]