from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsAuthorOrReadOnly
from django.db.models import Count
from .pagination import PopularPostsPagination, PostPagination


class PostApiView(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
    pagination_class = PostPagination

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






    