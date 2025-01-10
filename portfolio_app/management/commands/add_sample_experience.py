from django.core.management.base import BaseCommand
from portfolio_app.models import Experience
from datetime import date

class Command(BaseCommand):
    help = 'Add sample experience data'

    def handle(self, *args, **kwargs):
        # Sample experiences
        experiences = [
            {
                'company': 'Tech Solutions Inc.',
                'position': 'Senior Python Developer',
                'description': 'Led a team of developers in building and maintaining large-scale web applications using Django and React.',
                'achievements': 'Improved application performance by 40%,Implemented CI/CD pipeline reducing deployment time by 60%,Mentored junior developers and conducted code reviews',
                'start_date': date(2021, 1, 1),
                'end_date': None,  # Current job
                'tools': 'Python, Django, React, Docker'
            },
            {
                'company': 'Digital Innovations Ltd.',
                'position': 'Full Stack Developer',
                'description': 'Developed and maintained multiple web applications for clients in various industries.',
                'achievements': 'Delivered 5 major projects ahead of schedule,Reduced server costs by 30% through optimization,Implemented automated testing improving code coverage to 90%',
                'start_date': date(2019, 3, 1),
                'end_date': date(2020, 12, 31),
                'tools': 'Python, Django, JavaScript, PostgreSQL'
            },
            {
                'company': 'StartUp Solutions',
                'position': 'Junior Developer',
                'description': 'Worked on developing new features and maintaining existing codebase for a SaaS platform.',
                'achievements': 'Developed key features used by 10k+ users,Reduced bug reports by 45% through better testing,Contributed to API documentation and developer guides',
                'start_date': date(2018, 6, 1),
                'end_date': date(2019, 2, 28),
                'tools': 'Python, Flask, MySQL, REST APIs'
            }
        ]

        for exp_data in experiences:
            Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults={
                    'description': exp_data['description'],
                    'achievements': exp_data['achievements'],
                    'start_date': exp_data['start_date'],
                    'end_date': exp_data['end_date'],
                    'tools': exp_data['tools']
                }
            )
            self.stdout.write(f'Added experience: {exp_data["position"]} at {exp_data["company"]}')

        self.stdout.write(self.style.SUCCESS('Successfully added sample experiences'))
