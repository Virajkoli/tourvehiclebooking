from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from booking.models import Booking
import os

class Command(BaseCommand):
    help = 'Test email template rendering'

    def handle(self, *args, **options):
        # Get the most recent booking
        try:
            booking = Booking.objects.latest('created_at')
            self.stdout.write(f"Testing with booking ID: {booking.id}")
            self.stdout.write(f"User: {booking.user.username}")
            self.stdout.write(f"Car: {booking.car.name}")
            self.stdout.write(f"Pickup: {booking.pickup_location}")
            self.stdout.write(f"Destination: {booking.destination}")
            
            # Test template rendering
            html_content = render_to_string('emails/booking_confirmation.html', {
                'booking': booking,
                'user': booking.user,
            })
            
            # Save to a test file for inspection
            test_file = 'test_email_output.html'
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.stdout.write(
                self.style.SUCCESS(f'Template rendered successfully! Check {test_file}')
            )
            
            # Show first 500 characters
            self.stdout.write("First 500 characters of rendered template:")
            self.stdout.write(html_content[:500])
            
        except Booking.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('No bookings found. Please create a booking first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            )