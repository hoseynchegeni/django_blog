from django.urls import path
from .views import  PostApiView, CategoryApiView
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('post/', PostListApiView.as_view(), name = 'post_list')
# ]

router = DefaultRouter()

router.register('post', PostApiView, basename= 'post')
router.register('category', CategoryApiView, basename= 'category')
urlpatterns = router.urls