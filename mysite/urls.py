from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import BookmarkView, SupportView, InquiryCreateView, InquiryUpdateView, SocialCreateView, SocialUpdateView, SocialDeleteView, SocialListView, SocialFormView, IndexView, RegisterView, UserLogoutView, UserLoginView, ServiceListView, ServiceCreateView, ServiceEditView, ServiceDeleteView, PortfolioView, PortfolioUpdateView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('servfolio/', IndexView.as_view(), name='index'),
    path('servfolio/register/', RegisterView.as_view(), name='register'),
    path('servfolio/logout/', UserLogoutView.as_view(), name='logout'),
    path('servfolio/login/', UserLoginView.as_view(), name='login'),
    path('servfolio/services/', ServiceListView.as_view(), name='service'),
    path('servfolio/services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('servfolio/services/update/<int:pk>/', ServiceEditView.as_view(), name='service_update'),
    path('servfolio/services/delete/<int:pk>/', ServiceDeleteView.as_view(), name='service_delete'),
    path('servfolio/services/inquiry/<int:pk>/', InquiryCreateView.as_view(), name='inquiry_create' ),
    path('servfolio/service/inquiry/<int:pk>/update/', InquiryUpdateView.as_view(), name='inquiry_update'),
    path('servfolio/services/<int:pk>/bookmark', BookmarkView.as_view(), name='bookmark_view'),
    path('servfolio/services/<int:pk>/support/', SupportView.as_view(), name='support_view'),
    path('servfolio/<str:username>/index/', PortfolioView.as_view(), name='portfolio'),
    path('servfolio/<str:username>/projects/', ProjectListView.as_view(), name='project' ),
    path('servfolio/projects/create/', ProjectCreateView.as_view(), name='project_create' ),
    path('servfolio/projects/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('servfolio/projects/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('servfolio/<int:pk>/update/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('servfolio/social/form/', SocialFormView.as_view(), name='social_form'),
    path('servfolio/social/create/', SocialCreateView.as_view(), name='social_create'),
    path('servfolio/socials/<str:username>', SocialListView.as_view(), name='social'),
    path('servfolio/socials/update/<int:pk>', SocialUpdateView.as_view(), name='social_update'),
    path('servfolio/socials/delete/<int:pk>', SocialDeleteView.as_view(), name='social_delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

