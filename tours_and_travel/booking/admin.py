from django.contrib import admin
from .models import Car, Announcement, Booking, Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "license_number", "experience_years", "is_available")
    list_filter = ("is_available", "experience_years")
    search_fields = ("name", "phone_number", "license_number")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "price_per_km", "discount", "assigned_driver", "is_available")
    list_filter = ("is_available", "assigned_driver")
    search_fields = ("name", "model")


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")
    ordering = ("-date_posted",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "destination", "distance_km", "total_price", "booking_date", "pickup_time", "created_at")
    list_filter = ("booking_date", "created_at")
    search_fields = ("user__username", "car__name", "pickup_location", "destination")
    readonly_fields = ("total_price", "created_at")
    list_filter = ("booking_date", "car")
    search_fields = ("user__username", "car__name", "pickup_location")
