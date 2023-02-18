from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsAuthorOrReadOnly
from django.db.models import Count
from .pagination import PopularPostsPagination, PostPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class PostApiView(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['category__name']

class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class PopularPostsAPi(ListAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(like_count = Count('like')).order_by('-like_count')
    pagination_class = PopularPostsPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)






    