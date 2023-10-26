"""
URL configuration for pp4_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from my_pf import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as allauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_all, name='all'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/', include('allauth.urls')),
    path('home/', views.display_all, name='home'),
    path('edit-personal-details/', views.display_edit_personal_details, name='edit-personal-details'),
    path('me-irl/', views.display_me_irl, name='me-irl'),
    path('edit-headings/', views.display_edit_headings, name='edit-headings'),
    path('add-project/', views.add_project, name='add-project'),
    path('add-skill/', views.add_skill, name='add-skill'),
    path('edit-skills/', views.display_edit_skills, name='edit-skills'),
    path('edit-skills/<skill_id>/', views.display_edit_skills, name='edit-skills'),
    path('delete-skill/', views.delete_skill, name='delete-skill'),
    path('delete-skill/<skill_id>/', views.delete_skill, name='delete-skill'),
    path('edit-projects/', views.display_edit_projects, name='edit-projects'),
    path('edit-projects/<project_id>/', views.display_edit_projects, name='edit-projects'),
    path('delete-project/', views.delete_project, name='delete-project'),
    path('delete-project/<project_id>/', views.delete_project, name='delete-project')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
