from django.core.management.base import BaseCommand
from booking.models import Driver, Car

class Command(BaseCommand):
    help = 'Create sample drivers and assign them to cars'

    def handle(self, *args, **options):
        # Create sample drivers
        drivers_data = [
            {
                'name': 'John Smith',
                'phone_number': '+1-555-0123',
                'email': 'john.smith@toursandtravel.com',
                'license_number': 'DL123456789',
                'experience_years': 8
            },
            {
                'name': 'Maria Rodriguez',
                'phone_number': '+1-555-0124',
                'email': 'maria.rodriguez@toursandtravel.com',
                'license_number': 'DL987654321',
                'experience_years': 5
            },
            {
                'name': 'Ahmed Hassan',
                'phone_number': '+1-555-0125',
                'email': 'ahmed.hassan@toursandtravel.com',
                'license_number': 'DL456789123',
                'experience_years': 12
            },
            {
                'name': 'Emily Chen',
                'phone_number': '+1-555-0126',
                'email': 'emily.chen@toursandtravel.com',
                'license_number': 'DL789123456',
                'experience_years': 6
            },
            {
                'name': 'Robert Johnson',
                'phone_number': '+1-555-0127',
                'email': 'robert.johnson@toursandtravel.com',
                'license_number': 'DL321654987',
                'experience_years': 15
            }
        ]

        drivers = []
        for driver_data in drivers_data:
            driver, created = Driver.objects.get_or_create(
                phone_number=driver_data['phone_number'],
                defaults=driver_data
            )
            drivers.append(driver)
            if created:
                self.stdout.write(f'Created driver: {driver.name}')
            else:
                self.stdout.write(f'Driver already exists: {driver.name}')

        # Assign drivers to cars
        cars = Car.objects.all()
        for i, car in enumerate(cars):
            if i < len(drivers):
                car.assigned_driver = drivers[i]
                car.save()
                self.stdout.write(f'Assigned {drivers[i].name} to {car.name}')

        self.stdout.write(self.style.SUCCESS('Successfully created drivers and assigned them to cars!'))