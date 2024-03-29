"""
URL configuration for Softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from API import views
from authentication import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

# Create a router and register viewsets with it
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contributors', ContributorViewSet, basename='contributor')
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('users/', auth_views.UserListCreateView.as_view(), name='users-list'),
    path('user/<int:pk>/', auth_views.UserDetailView.as_view(), name='user-details'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', auth_views.SignupView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
