"""bceapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from bce import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', include('bce.urls')),
    # path('', views.index, name='index'),
    # path('login', views.index, name='index'),
    # path('risks', views.index, name='index'),
    # path('risks-types', views.index, name='index'),
    #
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name='home')
    # path('api-auth/', include('rest_framework.urls')),
    # path('admin/', admin.site.urls),
]
