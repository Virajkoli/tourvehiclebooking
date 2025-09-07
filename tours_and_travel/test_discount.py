from booking.models import Car

print("=== Discount Calculation Test ===")
print()

# Test examples
test_cases = [
    {"price": 100, "discount": 10, "expected": 90},
    {"price": 60, "discount": 15, "expected": 51},
    {"price": 35, "discount": 10, "expected": 31.5},
    {"price": 120, "discount": 5, "expected": 114},
]

print("Manual calculation tests:")
for test in test_cases:
    calculated = test["price"] * (100 - test["discount"]) / 100
    print(f"${test['price']} with {test['discount']}% discount = ${calculated} (expected: ${test['expected']})")
    print(f"✅ Correct" if calculated == test["expected"] else f"❌ Wrong")
    print()

print("Actual car data from database:")
for car in Car.objects.all()[:3]:
    if car.discount:
        manual_calc = float(car.price_per_day) * (100 - car.discount) / 100
        model_calc = float(car.discounted_price)
        print(f"Car: {car.name}")
        print(f"Original price: ${car.price_per_day}")
        print(f"Discount: {car.discount}%")
        print(f"Manual calculation: ${manual_calc:.2f}")
        print(f"Model calculation: ${model_calc:.2f}")
        print(f"Match: {'✅' if abs(manual_calc - model_calc) < 0.01 else '❌'}")
        print()
