from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'status', 'created_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
