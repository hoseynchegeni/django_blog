from django.urls import path
from .views import PostListApiView


urlpatterns = [
    path('post/', PostListApiView.as_view(), name = 'post_list')
]