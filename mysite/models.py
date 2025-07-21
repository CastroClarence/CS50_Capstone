from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category_choices = {
    "Web Development": "Web Development",
    "Software Development": "Software Development",
    "Design and Architecture" : "Design and Architecture",
    "Graphic Design" : "Graphic Design" 
}

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=64, choices=category_choices)
    image = models.ImageField(upload_to='service/', blank=True)

    def __str__(self):
        return f'{self.name}'
    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/', blank=True)
    
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio')
    profile_picture = models.ImageField(upload_to='portfolio/', blank=True)
    description = models.TextField()

class Social(models.Model):
    choices = {
        'Facebook': 'Facebook',
        'LinkedIn': 'LinkedIn',
        'Instagram': 'Instagram',
        'Github': 'Github',
        'X': 'X'
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    name = models.CharField(max_length=255, choices=choices )
    url = models.URLField()