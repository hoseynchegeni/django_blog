from django.urls import path
from .views import  PostApiView, CategoryApiView, PopularPostsAPi
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()

router.register('post', PostApiView, basename= 'post')
router.register('category', CategoryApiView, basename= 'category')


urlpatterns = [
    path('popular-posts/', PopularPostsAPi.as_view(), name= 'popular_posts')
]

urlpatterns += router.urls