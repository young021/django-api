"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from wordcount import views
# from rest_framework.urlpatterns import format_suffix_patterns

# from rest_framework.routers import DefaultRouter
# from django.urls import include,path
# from wordcount import views

from django.contrib import admin
from django.urls import path,include
from wordcount import urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls
import wordcount



urlpatterns = [
    path('',include('wordcount.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT )