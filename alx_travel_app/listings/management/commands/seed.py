import random
from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking, Review

# Get the User model
User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample data for the travel app'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Starting database seeding...'))

        # --- 1. Clear Old Data ---
        self.stdout.write('Clearing old data...')
        try:
            Review.objects.all().delete()
            Booking.objects.all().delete()
            Listing.objects.all().delete()
            # Keep superusers, delete regular users
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(self.style.SUCCESS('Successfully cleared old data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error clearing data: {e}'))
            return

        # --- 2. Create Sample Users ---
        self.stdout.write('Creating sample users...')
        try:
            host1 = User.objects.create_user(
                username='host_user1',
                email='host1@example.com',
                password='password123'
            )
            host2 = User.objects.create_user(
                username='host_user2',
                email='host2@example.com',
                password='password123'
            )
            guest1 = User.objects.create_user(
                username='guest_user1',
                email='guest1@example.com',
                password='password123'
            )
            guest2 = User.objects.create_user(
                username='guest_user2',
                email='guest2@example.com',
                password='password123'
            )
            self.stdout.write(self.style.SUCCESS('Sample users created.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating users: {e}'))
            return

        # --- 3. Create Sample Listings ---
        self.stdout.write('Creating sample listings...')
        try:
            listing1 = Listing.objects.create(
                host=host1,
                title='Cozy Beachfront Condo',
                description='A beautiful condo right on the beach. Perfect for a summer getaway.',
                address='123 Ocean Drive',
                city='Miami',
                country='USA',
                price_per_night=Decimal('250.00'),
                max_guests=4,
                bedrooms=2,
                bathrooms=2
            )

            listing2 = Listing.objects.create(
                host=host2,
                title='Modern Downtown Loft',
                description='A stylish loft in the heart of the city. Close to all attractions.',
                address='456 Main Street',
                city='New York',
                country='USA',
                price_per_night=Decimal('350.00'),
                max_guests=2,
                bedrooms=1,
                bathrooms=1
            )

            listing3 = Listing.objects.create(
                host=host1,
                title='Secluded Mountain Cabin',
                description='Escape to this quiet cabin in the mountains. Great for hiking.',
                address='789 Pine Road',
                city='Asheville',
                country='USA',
                price_per_night=Decimal('180.00'),
                max_guests=6,
                bedrooms=3,
                bathrooms=2
            )
            self.stdout.write(self.style.SUCCESS('Sample listings created.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating listings: {e}'))
            return

        # --- 4. Create Sample Bookings ---
        self.stdout.write('Creating sample bookings...')
        try:
            today = date.today()
            Booking.objects.create(
                guest=guest1,
                listing=listing1,
                check_in_date=today + timedelta(days=10),
                check_out_date=today + timedelta(days=15),
                status=Booking.BookingStatus.CONFIRMED
            )

            Booking.objects.create(
                guest=guest2,
                listing=listing2,
                check_in_date=today + timedelta(days=30),
                check_out_date=today + timedelta(days=35),
                status=Booking.BookingStatus.PENDING
            )

            Booking.objects.create(
                guest=guest1,
                listing=listing3,
                check_in_date=today + timedelta(days=5),
                check_out_date=today + timedelta(days=8),
                status=Booking.BookingStatus.CONFIRMED
            )
            self.stdout.write(self.style.SUCCESS('Sample bookings created.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating bookings: {e}'))
            return

        # --- 5. Create Sample Reviews ---
        self.stdout.write('Creating sample reviews...')
        try:
            Review.objects.create(
                guest=guest1,
                listing=listing3,
                rating=5,
                comment='Absolutely loved this cabin! So peaceful and clean. The host was great.'
            )

            Review.objects.create(
                guest=guest2,
                listing=listing1,
                rating=4,
                comment='Great location, but the place was a bit smaller than expected. Still had a good time.'
            )
            self.stdout.write(self.style.SUCCESS('Sample reviews created.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating reviews: {e}'))
            return

        # --- Final Success Message ---
        self.stdout.write(self.style.SUCCESS(
            'Database seeding completed successfully!'
        ))
        
        