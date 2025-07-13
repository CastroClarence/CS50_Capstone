from django.contrib import admin
from .models import Service, Portfolio, Project

# Register your models here.

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Project)