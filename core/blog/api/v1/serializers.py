from rest_framework import serializers
from ...models import Post, Category

class PostListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many = False, slug_field= "name", queryset = Category.objects.all())
    class Meta:
        model = Post
        fields = [  
            "author",
            "image",
            "title",
            "content",
            "status",
            "category",
            "created_date",
            "updated_date",
            "published_date",]
        
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["state"] = "list"
        if request.parser_context.get("kwargs").get("pk"):
            rep["state"] = "single"
            rep.pop("absolute_url", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
