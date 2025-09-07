from django.db import migrations


def seed_data(apps, schema_editor):
    Car = apps.get_model('booking', 'Car')
    Announcement = apps.get_model('booking', 'Announcement')

    if not Announcement.objects.exists():
        Announcement.objects.create(
            title='Welcome to Tours & Travel',
            content='Find the perfect car for your trip and book instantly.'
        )

    if not Car.objects.exists():
        placeholders = [
            {
                'name': 'City Compact',
                'model': 'Toyota Yaris',
                'price_per_day': 35.00,
                'discount': 10,
                'image': 'https://via.placeholder.com/600x400?text=City+Compact',
                'is_available': True,
            },
            {
                'name': 'Family SUV',
                'model': 'Honda CR-V',
                'price_per_day': 60.00,
                'discount': 15,
                'image': 'https://via.placeholder.com/600x400?text=Family+SUV',
                'is_available': True,
            },
            {
                'name': 'Luxury Sedan',
                'model': 'BMW 5 Series',
                'price_per_day': 120.00,
                'discount': 5,
                'image': 'https://via.placeholder.com/600x400?text=Luxury+Sedan',
                'is_available': True,
            },
        ]
        for c in placeholders:
            Car.objects.create(**c)


def unseed_data(apps, schema_editor):
    Car = apps.get_model('booking', 'Car')
    Announcement = apps.get_model('booking', 'Announcement')
    Car.objects.all().delete()
    Announcement.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
