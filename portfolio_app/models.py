from django.db import models
from django.shortcuts import render

class Certification(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-end_date']

    def __str__(self):
        return f"{self.title} - {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    key_features = models.TextField()
    technologies = models.CharField(max_length=200)
    project_link = models.URLField(blank=True, null=True)  # New field for project link
    github_link = models.URLField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title    

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    achievements = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    tools = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Personal Details'

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Technical'),
        ('SOFT', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"