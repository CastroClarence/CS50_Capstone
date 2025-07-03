from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from .forms import RegisterForm, CustomLoginForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'

class RegisterView(CreateView):
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'pages/login.html'
    next_page = reverse_lazy('index')