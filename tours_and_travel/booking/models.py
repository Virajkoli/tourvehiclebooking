from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0, help_text="Percentage discount")
    # Using URLField to keep dependencies minimal; you can switch to ImageField if Pillow is installed
    image = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.model})"

    @property
    def discounted_price(self):
        if self.discount:
            return self.price_per_day * (100 - self.discount) / 100
        return self.price_per_day


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
    booking_date = models.DateField()
    pickup_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name} on {self.booking_date}"
