from bce import views
from django.urls import include, path

urlpatterns = [path("api/", include("bce.urls")), path("", views.ApiRoot.as_view(), name="index")]
