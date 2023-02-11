from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null= True, blank= True)
    title = models.CharField(max_length= 255)
    content = models.TextField()
    status  = models.BooleanField()
    category = models.ForeignKey('Category', on_delete= models.SET_NULL, null= True, related_name= 'category')
    comments = models.ForeignKey('Comments', on_delete= models.SET_NULL, null= True, related_name= 'comments'),
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length= 255)

class Comment(models.Model):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    text = models.CharField(max_length= 500)
    created_date = models.DateTimeField(auto_now_add= True)

