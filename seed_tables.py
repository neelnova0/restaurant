import os
# pyrefly: ignore [missing-import]
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject1.settings')
django.setup()

from paradox.models import RestaurantTable

def seed():
    # Clear existing
    RestaurantTable.objects.all().delete()

    # Create 12 tables
    tables = [
        # Regular
        {'number': 1, 'capacity': 2, 'category': 'Regular', 'status': 'Available'},
        {'number': 2, 'capacity': 2, 'category': 'Regular', 'status': 'Occupied'},
        {'number': 3, 'capacity': 4, 'category': 'Regular', 'status': 'Available'},
        {'number': 4, 'capacity': 4, 'category': 'Regular', 'status': 'Reserved'},
        {'number': 5, 'capacity': 4, 'category': 'Regular', 'status': 'Available'},
        # Family
        {'number': 6, 'capacity': 6, 'category': 'Family', 'status': 'Available'},
        {'number': 7, 'capacity': 8, 'category': 'Family', 'status': 'Occupied'},
        {'number': 8, 'capacity': 6, 'category': 'Family', 'status': 'Reserved'},
        # VIP
        {'number': 9, 'capacity': 2, 'category': 'VIP', 'status': 'Available'},
        {'number': 10, 'capacity': 4, 'category': 'VIP', 'status': 'Reserved'},
        {'number': 11, 'capacity': 4, 'category': 'VIP', 'status': 'Occupied'},
        {'number': 12, 'capacity': 6, 'category': 'VIP', 'status': 'Available'},
    ]

    for t in tables:
        RestaurantTable.objects.create(**t)
    print("Successfully seeded 12 tables!")

if __name__ == '__main__':
    seed()
