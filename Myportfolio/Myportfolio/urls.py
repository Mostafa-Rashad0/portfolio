"""
URL configuration for Myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from page import views as page_views
from projects import views as projects_views
from contacts import views as contacts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_views.home, name='home'),
    path('projects/', projects_views.projects, name='projects'),
    path('contact/', contacts_views.contact, name='contact'),
    path('projects/<int:project_id>/', projects_views.eachproject, name='eachproject'),
    path('thanks/', contacts_views.thanks, name='thanks'),
]

# Add media URL configuration for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


