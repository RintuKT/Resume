from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import PersonalDetail, Project, Experience, Skill, Certification, Contact

def home(request):
    personal_detail = PersonalDetail.objects.first()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    certifications = Certification.objects.all().order_by('-end_date')
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save contact message
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Send email notification
        try:
            send_mail(
                f'New Contact Message from {name}',
                f'From: {name} <{email}>\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
