from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Car, Announcement, Booking
from .forms import BookingForm, RegisterForm


def home(request):
    announcements = Announcement.objects.order_by('-date_posted')[:5]
    cars = Car.objects.filter(is_available=True)[:6]
    return render(request, 'home.html', {"announcements": announcements, "cars": cars})


def car_list(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'cars/list.html', {"cars": cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/detail.html', {"car": car})


@login_required
def book_car(request, pk):
    car = get_object_or_404(Car, pk=pk, is_available=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.car = car
            booking.save()
            messages.success(request, 'Booking confirmed!')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/book.html', {"car": car, "form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'booking/my_bookings.html', {"bookings": bookings})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})
