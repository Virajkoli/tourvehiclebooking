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
    distance_km = forms.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={"step": "0.1", "min": "0.1"}),
        help_text="Distance in kilometers"
    )

    class Meta:
        model = Booking
        fields = ["pickup_location", "destination", "distance_km", "booking_date", "pickup_time"]
        widgets = {
            'pickup_location': forms.TextInput(attrs={'placeholder': 'Enter pickup location'}),
            'destination': forms.TextInput(attrs={'placeholder': 'Enter destination'}),
        }
