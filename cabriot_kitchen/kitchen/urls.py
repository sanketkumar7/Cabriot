from django.urls import path
from . import views
urlpatterns=[
    path('get_items/<str:section>/', views.get_items, name='get_items'),
    path('display/main',views.display_main_items_view,name='display_main'),
    path('display/vegetable',views.display_vegetables_view,name='display_vegetable'),
    path('display/bread',views.display_bread_view,name='display_bread'),
]