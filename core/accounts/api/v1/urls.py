from django.urls import path, include
from .views import RegistrationApiView, ChangePasswordView

app_name = 'api_v1'

urlpatterns = [
    path('registration',RegistrationApiView.as_view(),name= 'registration'),
    path('change-password', ChangePasswordView.as_view(), name= 'change-password')
]