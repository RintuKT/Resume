from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import PersonalDetail, Project, Experience, Skill, Certification, Contact

def home(request):
    personal_detail = PersonalDetail.objects.first()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    certifications = Certification.objects.all().order_by('end_date')
    context = {
        'personal_detail': personal_detail,
        'skills': skills,
        'certifications': certifications,
    }
    return render(request, 'portfolio_app/home.html', context)

def personal_detail(request):
    personal_detail = PersonalDetail.objects.first()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    context = {
        'personal_detail': personal_detail,
        'skills': skills,
    }
    return render(request, 'portfolio_app/personaldetail.html', context)

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio_app/projects.html', context)

def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')  # Changed to reverse order
    personal_detail = PersonalDetail.objects.first()
    context = {
        'experiences': experiences,
        'personal_detail': personal_detail,
    }
    return render(request, 'portfolio_app/experience.html', context)

def contact(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            # Get form data
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()
            
            # Validate form data
            if not all([name, email, message]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please fill in all required fields.'
                })
            
            # Save to database
            contact = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            # Send email
            try:
                subject = f'New Contact Message from {name}'
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True  # Changed to True to prevent email errors from breaking the flow
                )
            except Exception as e:
                print(f"Email sending failed: {str(e)}")
                # Continue even if email fails
            
            # Return success response
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been received.'
            })
            
        except Exception as e:
            print(f"Contact form error: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred. Please try again.'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    })
