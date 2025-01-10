from django.contrib import admin
from .models import PersonalDetail, Project, Experience, Skill, Certification

@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'github_link', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'technologies')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('position', 'company', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    list_editable = ('proficiency',)
    search_fields = ('name',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'start_date', 'end_date')
    list_filter = ('institution',)
    search_fields = ('title', 'institution')
