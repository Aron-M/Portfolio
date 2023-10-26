from django.contrib import admin
from .models import PersonalDetails, Headings, Project, Skills, SkillCategory


admin.site.register(PersonalDetails)
admin.site.register(Headings)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(SkillCategory)
