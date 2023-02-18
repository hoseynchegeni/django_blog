from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null= True, blank= True)
    title = models.CharField(max_length= 255)
    content = models.TextField()
    status  = models.BooleanField()
    category = models.ForeignKey('Category', on_delete= models.SET_NULL, null= True, related_name= 'category')
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField()
    like = models.ManyToManyField('accounts.User', blank= True, related_name= 'like_post')
    like_counter = models.PositiveBigIntegerField(default= 0)

    def __str__(self):
        return self.title
    
    def like_counter(self):
        return self.like.count()


class Category(models.Model):
    name = models.CharField(max_length= 255)
    url = models.CharField(max_length= 255, default='#')

