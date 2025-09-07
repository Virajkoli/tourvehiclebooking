from booking.models import Car

print("=== Car Images Debug ===")
for car in Car.objects.all():
    print(f"Car: {car.name}")
    print(f"Image URL: '{car.image}'")
    print(f"Image is empty: {not car.image}")
    print(f"Image length: {len(car.image) if car.image else 0}")
    print("---")
