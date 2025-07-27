from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Service, Portfolio, Project, Social, Inquiry

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'class': 'input',
        })
        self.fields["last_name"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["username"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["password1"].widget.attrs.update({
            'class': 'input'
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'input'
        })

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input'
        })

class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'category', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class' : 'input'
        })
        self.fields['category'].widget.attrs.update({
            'class' : 'input'
        })
        self.fields['image'].widget.attrs.update({
            'class' : 'file-input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'textarea'
        })

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['description','profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({
            'class' : 'file-input'
        })
        self.fields['description'].widget.attrs.update({
            'class' : 'textarea'
        })

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'service', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'input'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'textarea'
        })
        self.fields['service'].widget.attrs.update({
            'class': 'input'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'file-input'
        })

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['name', 'url']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class' : 'textarea'
        })