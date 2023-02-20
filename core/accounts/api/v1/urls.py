from django.urls import path, include
from .views import RegistrationApiView, ChangePasswordView, ProfileApiView,ProfileList

app_name = 'api_v1'

urlpatterns = [
    path('registration',RegistrationApiView.as_view(),name= 'registration'),
    path('change-password', ChangePasswordView.as_view(), name= 'change-password'),
    path('profile', ProfileApiView.as_view(), name= 'profile'),
    path('profile-list', ProfileList.as_view(), name= 'profile-list')

]