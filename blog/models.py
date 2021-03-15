from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to= 'images')
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    starter = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.commenter} commented on {self.post}"



