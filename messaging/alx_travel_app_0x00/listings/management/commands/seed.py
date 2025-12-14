from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed database with sample listings"

    def handle(self, *args, **kwargs):
        listings_data = [
            {
                "title": "Beachside Villa",
                "description": "Beautiful villa near the ocean",
                "location": "Mombasa",
                "price_per_night": 150.00,
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin with mountain views",
                "location": "Naivasha",
                "price_per_night": 90.00,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in city center",
                "location": "Nairobi",
                "price_per_night": 120.00,
            },
        ]

        for data in listings_data:
            Listing.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS("Database seeded successfully!")
        )
