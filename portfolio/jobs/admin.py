from django.contrib import admin
from .models import Job
from .models import Project

# Register your models here.
admin.site.register(Job)
admin.site.register(Project)