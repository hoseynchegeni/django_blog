from django.urls import path, include
from .views import PostListApiView

app_name = 'blog'

urlpatterns = [
    path('', PostListApiView.as_view(), name = ('post_lits')),
    path('api/v1/', include('blog.api.v1.urls'), name= 'api_v1'),
]