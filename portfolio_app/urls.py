from django.urls import path
from . import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', views.personal_detail, name='personal_detail'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
]