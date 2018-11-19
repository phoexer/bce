from django.urls import path
from bce import views
# from bce.authentication import CustomAuthToken
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ApiRoot.as_view()),
    # path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('risk-types/',
         views.RiskTypeList.as_view(),
         name='risk-type-list'),
    path('risk-types/<int:pk>/',
         views.RiskTypeDetail.as_view(),
         name='risk-type-detail'),
    path('risks/',
         views.RiskList.as_view(),
         name='risk-list'),
    path('risks/<int:pk>/',
         views.RiskDetail.as_view(),
         name='risk-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
