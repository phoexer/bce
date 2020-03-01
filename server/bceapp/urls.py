from bce import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("bce.urls")),
    url("admin/", admin.site.urls),
    path("", views.ApiRoot.as_view(), name="index"),
]
