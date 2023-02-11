from rest_framework import serializers
from ...models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [  
            "author",
            "image",
            "title",
            "content",
            "status",
            "created_date",
            "updated_date",
            "published_date",]