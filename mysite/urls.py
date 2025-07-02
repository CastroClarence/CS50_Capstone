from django.urls import path
from .views import *

urlpatterns = [
    path('servfolio/', IndexView.as_view(), name='index'),
]
