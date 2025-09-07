from django.contrib import admin
from .models import Car, Announcement, Booking


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "price_per_day", "discount", "is_available")
    list_filter = ("is_available",)
    search_fields = ("name", "model")


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")
    ordering = ("-date_posted",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "booking_date", "pickup_time", "pickup_location", "created_at")
    list_filter = ("booking_date", "car")
    search_fields = ("user__username", "car__name", "pickup_location")
