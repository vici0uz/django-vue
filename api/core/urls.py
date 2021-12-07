from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'core'

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    ]
