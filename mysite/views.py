from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from .forms import RegisterForm, CustomLoginForm, ServiceCreateForm, PortfolioForm, ProjectForm, SocialForm, InquiryForm
from .models import Service, Portfolio, Social, Project, Inquiry, Bookmark, Support
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect


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

class ServiceView(ListView):
    model = Service
    template_name = 'portfolio/service.html'

    def get_queryset(self):
        self.owner = get_object_or_404(User, username=self.kwargs['username'])
        return Service.objects.filter(user = self.owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_form'] = ServiceCreateForm
        context['owner'] = self.owner
        context['is_owner'] = self.request.user == self.owner
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class ServiceListView(ListView):
    # Shows all users' Services
    model = Service
    template_name = 'pages/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['service_form'] = ServiceCreateForm()
        context['inquiry_form'] = InquiryForm()
        context['service_bookmarked'] = list(Bookmark.objects.filter(user = self.request.user).values_list('service_id', flat=True))
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
        self.user = get_object_or_404(User, username = username)
        return get_object_or_404(Portfolio, user = self.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.user
        context['portfolio_form'] = PortfolioForm
        return context
    
class PortfolioCreateView(CreateView):
    model = Portfolio
    template_name = 'portfolio/portfolio_create.html'
    form_class = PortfolioForm

    def get_success_url(self):
        return reverse_lazy(
            'portfolio', kwargs={
                'username' : self.request.user
            }
        )
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
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
        service = Service.objects.get(id = self.kwargs['pk'])
        self.owner = get_object_or_404(User, username=self.kwargs['username'])
        projects = Project.objects.filter(user = self.owner, service = service)
        if projects:
            return projects
        else:
            return None

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
        return reverse_lazy('service_user', kwargs={
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
    
class SocialFormView(FormView):
    template_name = 'portfolio/social_form.html'
    form_class = SocialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'social', kwargs={
                'username' : self.request.user.username
            })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.user
        return context

    
class SocialCreateView(CreateView):
    # This is for on the modal of the social page
    # For users who already have first existing social
    form_class = SocialForm
    model = Social


    def get_success_url(self):
        return reverse_lazy(
            'social', kwargs={
                'username' : self.request.user.username
            })
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponseRedirect(
                reverse('social', kwargs={
                    'username': self.request.user.username
                })
            )
        
class SocialListView(ListView):
    model = Social
    template_name = 'portfolio/social.html'

    def get_queryset(self):
        self.owner = get_object_or_404(User, username=self.kwargs['username']) 
        return Social.objects.filter(user=self.owner)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.owner
        context['social_form'] = SocialForm
        return context
    
class SocialUpdateView(UpdateView):
    model = Social
    form_class = SocialForm

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('social', kwargs={
            'username' : username
        })
    
class SocialDeleteView(DeleteView):
    model = Social
    
    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy('social', kwargs={
            'username' : username
        })

class InquiryCreateView(CreateView):
    model = Inquiry
    success_url = reverse_lazy('service')
    form_class = InquiryForm

    def form_valid(self, form):
        service = self.kwargs['pk']
        form.instance.user = self.request.user
        form.instance.service = get_object_or_404(Service, pk=service)
        return super().form_valid(form)
    
class InquiryUpdateView(UpdateView):
    model = Inquiry
    fields = []
    success_url = reverse_lazy('service')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        action = request.POST.get('action')
        if action == 'Approved':
            self.object.status = 'Approved'
        elif action == 'Declined':
            self.object.status = 'Declined'
        self.object.read = 'True'
        self.object.save()

        return redirect(self.success_url)
    
@method_decorator(csrf_protect, name='dispatch')
class BookmarkView(View):
    def post(self, request, *args, **kwargs):
        service = get_object_or_404(Service, id=kwargs['pk'])
        bookmark, created = Bookmark.objects.get_or_create(
            user = request.user,
            service = service
        )
        bookmark.status = not bookmark.status
        bookmark.save()
        return JsonResponse({
            'success': True,
            'status' : bookmark.status
        })
    
class SupportView(View):
    def post(self, request, **kwargs):
        service = Service.objects.get(id = kwargs['pk'])
        support, created = Support.objects.get_or_create(user = request.user, service = service)
        support.status = not support.status
        support.save()
        return JsonResponse({
            'success' : True,
            'status' : support.status
        })