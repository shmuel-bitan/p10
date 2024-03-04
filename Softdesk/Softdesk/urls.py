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

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', auth_views.SignupView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('contributors/', views.ContributorListCreateView.as_view(), name='contributor-list'),
    path('contributors/<int:pk>/', views.ContributorDetailView.as_view(), name='contributor-detail'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('issues/', views.IssueListCreateView.as_view(), name='issue-list'),
    path('issues/<int:pk>/', views.IssueDetailView.as_view(), name='issue-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
]
