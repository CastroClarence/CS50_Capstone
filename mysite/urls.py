from django.urls import path
from .views import IndexView, RegisterView, UserLogoutView, UserLoginView

urlpatterns = [
    path('servfolio/', IndexView.as_view(), name='index'),
    path('servfolio/register/', RegisterView.as_view(), name='register'),
    path('servfolio/logout/', UserLogoutView.as_view(), name='logout'),
    path('servfolio/login/', UserLoginView.as_view(), name='login'),
]
