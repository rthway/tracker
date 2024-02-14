from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_serial_numbers, name='generate_serial_numbers'),
    path('list/', views.serial_number_list, name='serial_number_list'),
]
