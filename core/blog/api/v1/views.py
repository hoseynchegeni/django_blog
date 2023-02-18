from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework.response import Response 
from .permissions import IsAuthorOrReadOnly
from django.db.models import Count
from .pagination import PopularPostsPagination


class PostApiView(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)


class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PopularPostsAPi(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(like_count = Count('like')).order_by('-like_count')
    pagination_class = PopularPostsPagination






    