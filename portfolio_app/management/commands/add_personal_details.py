from django.core.management.base import BaseCommand
from portfolio_app.models import PersonalDetail

class Command(BaseCommand):
    help = 'Add personal details'

    def handle(self, *args, **kwargs):
        # Clear existing personal details
        PersonalDetail.objects.all().delete()
        
        personal_detail = PersonalDetail.objects.create(
            name='RINTU KT',
            title='Python Developer',
            bio='''Aspiring Python developer with expertise in building and optimising Ecommerce Webapp Skilled in 
Django, Html, CSS, Java script, Bootstrap. Proven track record of leading teams to success, driving efficiency improvements, 
and implementing innovative solutions for complex challenges. Passionate about leveraging technology to streamline operations, 
enhance productivity, and deliver high-quality solutions that exceed client expectations.''',
            email='rintuiri@gmail.com',
            phone='+918089526160',
            location='Iringalloor,Calicut-14',
            linkedin='linkedin.com/in/rintukt',
            github='Link'  # Replace with your actual GitHub link
        )
        
        self.stdout.write(f'Added personal details for {personal_detail.name}')
