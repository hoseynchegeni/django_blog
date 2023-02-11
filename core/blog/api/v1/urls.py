from django.urls import path
from .views import PostListApiView, PostViewSet
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('post/', PostListApiView.as_view(), name = 'post_list')
# ]

router = DefaultRouter()

router.register('post', PostViewSet, basename= 'post')
urlpatterns = router.urls