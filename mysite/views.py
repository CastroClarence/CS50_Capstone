from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from .forms import RegisterForm, CustomLoginForm, ServiceCreateForm, PortfolioForm, ProjectForm
from .models import Service, Portfolio, Social, Project
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

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

@method_decorator(login_required(login_url='login'), name='dispatch')
class ServiceListView(ListView):
    model = Service
    template_name = 'pages/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_form'] = ServiceCreateForm()
        return context
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'pages/service.html'

    def get_success_url(self):
        return reverse_lazy('service')

    def form_valid(self, form):
        print("FORM IS VALID", form.cleaned_data)
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Successfully created service.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Failed creating service.')
        return super().form_invalid(form)

@method_decorator(login_required(login_url='login'), name= 'dispatch')
class ServiceEditView(UpdateView):
    model = Service
    form_class = ServiceCreateForm

    def get_success_url(self):
        return reverse_lazy('service')
    
    def form_valid(self, form):
        if not form.cleaned_data.get('image') and self.object.image:
            form.instance.image = self.object.image
        return super().form_valid(form)
    
@method_decorator(login_required(login_url='login'), name= 'dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service')

    def form_valid(self, form):
        form
        messages.add_message(self.request, messages.SUCCESS, 'Service deleted successfully.')
        return super().form_valid(form)
    
class PortfolioView(DetailView):
    template_name = 'portfolio/portfolio.html'
    model = Portfolio
    
    def get_object(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username = username)
        return get_object_or_404(Portfolio, user = user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_form'] = PortfolioForm
        return context
    
class PortfolioUpdateView(UpdateView):
    model = Portfolio
    form_class = PortfolioForm

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('portfolio', kwargs={
            'username': username
        })
    
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project.html'

    def get_queryset(self):
        self.owner = get_object_or_404(User, username=self.kwargs['username'])
        return Project.objects.filter(user = self.owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_form'] = ProjectForm
        context['owner'] = self.owner
        context['is_owner'] = self.request.user == self.owner
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    
    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('project', kwargs={
            'username' : username
        })
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('project', kwargs={
            'username' : username
        })
    
class ProjectDeleteView(DeleteView):
    model = Project

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('project', kwargs={
            'username': username
        })
    