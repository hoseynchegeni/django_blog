from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostListSerializer
from ...models import Post
from rest_framework.response import Response 


class PostListApiView(APIView):
    serializer_class = PostListSerializer

    def get(self, request):
        posts = Post.objects.filter(status = True)
        serializer = self.serializer_class(posts, many = True)
        return Response (serializer.data)
    

class PostViewSet(ModelViewSet):
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(status = True)

    