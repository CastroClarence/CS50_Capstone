from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView, RegisterView, UserLogoutView, UserLoginView, ServiceListView, ServiceCreateView, ServiceEditView, ServiceDeleteView

urlpatterns = [
    path('servfolio/', IndexView.as_view(), name='index'),
    path('servfolio/register/', RegisterView.as_view(), name='register'),
    path('servfolio/logout/', UserLogoutView.as_view(), name='logout'),
    path('servfolio/login/', UserLoginView.as_view(), name='login'),
    path('servfolio/services/', ServiceListView.as_view(), name='service'),
    path('servfolio/services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('servfolio/services/update/<int:pk>', ServiceEditView.as_view(), name='service_update'),
    path('servfolio/services/delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

