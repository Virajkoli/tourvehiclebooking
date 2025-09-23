from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    license_number = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price_per_km = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0, help_text="Percentage discount")
    # Using URLField to keep dependencies minimal; you can switch to ImageField if Pillow is installed
    image = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.model})"

    @property
    def discounted_price_per_km(self):
        if self.discount:
            return self.price_per_km * (100 - self.discount) / 100
        return self.price_per_km


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255, default="Unknown Destination")
    distance_km = models.DecimalField(max_digits=6, decimal_places=2, default=20.0, help_text="Distance in kilometers")
    booking_date = models.DateField()
    pickup_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate total price based on distance and car price per km
        if self.distance_km and self.car:
            self.total_price = self.distance_km * self.car.discounted_price_per_km
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.car.name} on {self.booking_date}"
