from django.core.management.base import BaseCommand
from portfolio_app.models import Skill

class Command(BaseCommand):
    help = 'Add initial skills data'

    def handle(self, *args, **kwargs):
        # Clear existing skills
        Skill.objects.all().delete()

        # Technical Skills
        technical_skills = [
            {'name': 'Python', 'proficiency': 90},
            {'name': 'JavaScript', 'proficiency': 85},
            {'name': 'HTML', 'proficiency': 85},
            {'name': 'CSS', 'proficiency': 85},
            {'name': 'Django', 'proficiency': 85},
            {'name': 'Bootstrap', 'proficiency': 80},
            {'name': 'Git', 'proficiency': 85},
            {'name': 'GitLab', 'proficiency': 80},
            {'name': 'GitHub', 'proficiency': 80},
            {'name': 'CodeCommit', 'proficiency': 75},
            {'name': 'MySQL', 'proficiency': 85},
            {'name': 'PostgreSQL', 'proficiency': 80},
            {'name': 'Shell Scripting (Bash)', 'proficiency': 75},
            {'name': 'ML', 'proficiency': 70},
            {'name': 'AI', 'proficiency': 70},
            {'name': 'SQL', 'proficiency': 85},
            {'name': 'Metabase', 'proficiency': 80},
            {'name': 'Katalon', 'proficiency': 80},
            {'name': 'Notion', 'proficiency': 85},
            {'name': 'VS Code', 'proficiency': 90},
            {'name': 'Selenium', 'proficiency': 80},
            {'name': 'Appium', 'proficiency': 75}
        ]

        # Soft Skills
        soft_skills = [
            {'name': 'Quick Learner', 'proficiency': 95},
            {'name': 'Team Player', 'proficiency': 90},
            {'name': 'Problem-solving', 'proficiency': 90},
            {'name': 'Multitasking', 'proficiency': 85},
            {'name': 'Good Communication', 'proficiency': 90},
            {'name': 'Research & Strategic Planning', 'proficiency': 85}
        ]

        # Add technical skills
        for skill_data in technical_skills:
            skill = Skill.objects.create(
                name=skill_data['name'],
                category='TECH',
                proficiency=skill_data['proficiency']
            )
            self.stdout.write(f'Added technical skill: {skill.name}')

        # Add soft skills
        for skill_data in soft_skills:
            skill = Skill.objects.create(
                name=skill_data['name'],
                category='SOFT',
                proficiency=skill_data['proficiency']
            )
            self.stdout.write(f'Added soft skill: {skill.name}')

        self.stdout.write(self.style.SUCCESS('Successfully added all skills'))
