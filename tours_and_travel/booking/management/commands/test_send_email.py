from django.core.management.base import BaseCommand
from booking.models import Booking
from booking.views import send_booking_confirmation_email

class Command(BaseCommand):
    help = 'Test sending an actual booking confirmation email'

    def handle(self, *args, **options):
        try:
            # Get the most recent booking
            booking = Booking.objects.latest('created_at')
            self.stdout.write(f"Testing email for booking ID: {booking.id}")
            self.stdout.write(f"User: {booking.user.username} ({booking.user.email})")
            
            # Send the email
            success = send_booking_confirmation_email(booking)
            
            if success:
                self.stdout.write(
                    self.style.SUCCESS(f'Email sent successfully to {booking.user.email}!')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('Failed to send email. Check console for errors.')
                )
                
        except Booking.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('No bookings found. Please create a booking first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            )