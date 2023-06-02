from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('car_list', views.car_list, name='car_list'),        
    path('car/<int:id>', views.car, name='car'),
]
