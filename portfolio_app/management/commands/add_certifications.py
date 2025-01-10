from django.core.management.base import BaseCommand
from portfolio_app.models import Certification
from datetime import date

class Command(BaseCommand):
    help = 'Add certification data'

    def handle(self, *args, **kwargs):
        # Clear existing certifications
        Certification.objects.all().delete()
        
        certifications = [
            {
                'title': 'Certification in Python Programming',
                'institution': 'Illinois Tech US',
                'start_date': date(2023, 8, 1),
                'end_date': date(2024, 10, 1),
                'description': 'Completed intensive training on Python programming fundamentals and advanced concepts.'
            },
            {
                'title': 'Python Programming',
                'institution': 'Entri Elevate',
                'start_date': date(2023, 8, 1),
                'end_date': date(2024, 10, 1),
                'description': '''• Completed 8 months of intensive training on Python, Django, and front-end development.
• Developed projects demonstrating practical applications using python with Django REST framework for both frontend and backend'''
            }
        ]

        for cert_data in certifications:
            certification = Certification.objects.create(**cert_data)
            self.stdout.write(f'Added certification: {certification.title} from {certification.institution}')

        self.stdout.write(self.style.SUCCESS('Successfully added certifications'))
