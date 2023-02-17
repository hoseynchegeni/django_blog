from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostListSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework.response import Response 


class PostApiView(ModelViewSet):
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(status = True)


class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    