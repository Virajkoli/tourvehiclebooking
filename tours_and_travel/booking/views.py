from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Car, Announcement, Booking
from .forms import BookingForm, RegisterForm


def send_booking_confirmation_email(booking):
    """Send booking confirmation email to the user"""
    try:
        # Render email templates
        html_message = render_to_string('emails/booking_confirmation.html', {
            'booking': booking,
            'user': booking.user,
        })
        plain_message = render_to_string('emails/booking_confirmation.txt', {
            'booking': booking,
            'user': booking.user,
        })
        
        # Send email
        send_mail(
            subject=f'🚗 Booking Confirmation - {booking.car.name}',
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[booking.user.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


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
            
            # Send confirmation email
            email_sent = send_booking_confirmation_email(booking)
            if email_sent:
                messages.success(request, 'Booking confirmed! Check your email for details.')
            else:
                messages.success(request, 'Booking confirmed! (Note: Email notification failed)')
            
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
