from django.urls import path
from .views import  PostApiView, CategoryApiView, PopularPostsAPi
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('post/', PostListApiView.as_view(), name = 'post_list')
# ]

router = DefaultRouter()

router.register('post', PostApiView, basename= 'post')
router.register('category', CategoryApiView, basename= 'category')
router.register('popular-posts', PopularPostsAPi, basename='popular_posts')
urlpatterns = router.urls