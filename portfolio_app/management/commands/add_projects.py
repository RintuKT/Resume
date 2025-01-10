from django.core.management.base import BaseCommand
from portfolio_app.models import Project

class Command(BaseCommand):
    help = 'Add project data'

    def handle(self, *args, **kwargs):
        # Clear existing projects
        Project.objects.all().delete()
        
        # Projects data
        projects = [
            {
                'title': 'E-Commerce Web Application',
                'description': 'Developed a full-featured e-commerce platform using Django, including product listings and user management. Styled the application using CSS and JavaScript to enhance the user experience.',
                'key_features': [
                    'Product listings and user management',
                    'Enhanced user experience with CSS and JavaScript',
                    'Data automation reducing manual consolidation by 25%',
                    'Quality assurance scripts for improved accuracy'
                ],
                'technologies': 'Python, Django, HTML, CSS, JavaScript, Bootstrap',
                'github_link': 'Link',  # Replace with actual GitHub link
                'image': '',  # Add project image if available
                'order': 1
            },
            {
                'title': 'Issue Tracker Web Application',
                'description': 'Developed a full-featured issue tracker using Django, including product listings and issue reporting. Styled the application using CSS and JavaScript to enhance the user experience.',
                'key_features': [
                    'Product listings and issue reporting functionality',
                    'Enhanced UI with CSS and JavaScript',
                    'On-time problem solving and status updating',
                    'CRE team integration for customer support'
                ],
                'technologies': 'Python, Django, HTML, CSS, JavaScript, Bootstrap',
                'github_link': 'Link',  # Replace with actual GitHub link
                'image': '',  # Add project image if available
                'order': 2
            }
        ]

        for project_data in projects:
            project = Project.objects.create(
                title=project_data['title'],
                description=project_data['description'],
                key_features='\n'.join(project_data['key_features']),
                technologies=project_data['technologies'],
                github_link=project_data['github_link'],
                image=project_data['image'],
                order=project_data['order']
            )
            self.stdout.write(f'Added project: {project.title}')

        self.stdout.write(self.style.SUCCESS('Successfully added projects'))
