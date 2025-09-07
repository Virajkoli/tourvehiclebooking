from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('cars/<int:pk>/book/', views.book_car, name='book_car'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
