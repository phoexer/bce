from django.urls import path
from bce import views
from bce.authentication import CustomAuthToken
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('risk-types/',
         views.RiskTypeList.as_view(),
         name='risk-type-list'),
    path('risk-types/<int:pk>/',
         views.RiskTypeDetail.as_view(),
         name='risk-type-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
