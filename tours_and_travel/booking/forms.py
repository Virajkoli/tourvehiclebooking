from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    pickup_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Booking
        fields = ["pickup_location", "booking_date", "pickup_time"]
