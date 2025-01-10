from django.core.management.base import BaseCommand
from portfolio_app.models import Experience
from datetime import date

class Command(BaseCommand):
    help = 'Add real experience data'

    def handle(self, *args, **kwargs):
        # Clear existing experiences
        Experience.objects.all().delete()

        experiences = [
            {
                'company': 'Eduport Pvt.Ltd',
                'position': 'Scrum Master',
                'description': '''Facilitated Agile ceremonies, including sprint planning, daily stand-ups, sprint reviews, and retrospectives, to ensure smooth project execution.''',
                'achievements': '''• Facilitated Agile ceremonies, including sprint planning, daily stand-ups, sprint reviews, and retrospectives, to ensure smooth project execution.
• Collaborated with Product Owners to refine and prioritize the product backlog, aligning deliverables with business goals.
• Identified and removed impediments to optimize team productivity and foster continuous improvement.''',
                'start_date': date(2024, 10, 1),
                'end_date': None,
                'tools': 'Python, SQL, Metabase, Katalon, Selenium, Appium, Notion, Jira, Git, VS Code'
            },
            {
                'company': 'Eduport Pvt.Ltd',
                'position': 'Product Associate',
                'description': '''Market Research and Conduct meeting with inter departments, identify requirements and possibility''',
                'achievements': '''• Market Research and Conduct meeting with inter departments, identify requirements and possibility
• Provide actionable insights to guide product development and strategy
• Facilitate effective communication and coordination among teams
• Assist in developing and maintaining the product roadmap. Prioritize features and improvements based on customer and departmental needs
• Create and maintain detailed product documentation, including specifications, user guides, and training materials. Ensure all stakeholders are well-informed about product features and updates
• Collaborate with UX/UI designers to ensure a user-centric approach to product development. Contribute to creating intuitive and user-friendly interfaces''',
                'start_date': date(2024, 4, 1),
                'end_date': date(2024, 10, 1),
                'tools': 'Python, SQL, Metabase, Katalon, Selenium, Appium, Notion'
            },
            {
                'company': 'Eduport Pvt.Ltd',
                'position': 'Payment Coordinator',
                'description': '''Successive payment collection through Payment gateways continuous follow-up''',
                'achievements': '''• Successive payment collection through Payment gateways continuous follow-up
• Customer handling and Problem Solving
• Data management by excel
• Dealing with different clients by effective Communication''',
                'start_date': date(2022, 10, 1),
                'end_date': date(2024, 3, 1),
                'tools': ''
            }
        ]

        for exp_data in experiences:
            experience = Experience.objects.create(**exp_data)
            self.stdout.write(f'Added experience: {experience.position} at {experience.company}')

        self.stdout.write(self.style.SUCCESS('Successfully added experiences'))
