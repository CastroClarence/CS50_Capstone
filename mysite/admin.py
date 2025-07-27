from django.contrib import admin
from .models import Service, Portfolio, Project, Social, Inquiry

# Register your models here.

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Social)
admin.site.register(Inquiry)