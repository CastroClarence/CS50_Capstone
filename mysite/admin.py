from django.contrib import admin
from .models import Service, Portfolio, Project, Social

# Register your models here.

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Social)