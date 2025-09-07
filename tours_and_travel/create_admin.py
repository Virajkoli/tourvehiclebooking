from django.contrib.auth.models import User

# Make existing user 'Viraj' a superuser
try:
    user = User.objects.get(username='Viraj')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"✅ User '{user.username}' is now a superuser!")
except User.DoesNotExist:
    print("❌ User 'Viraj' not found")

# Or create a new superuser
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print("✅ Created superuser 'admin' with password 'admin123'")
