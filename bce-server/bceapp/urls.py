from bce import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', include('bce.urls')),
    path('', views.ApiRoot.as_view(), name='index'),
]
