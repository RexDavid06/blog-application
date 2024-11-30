from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    
    def comment_count(self):
        return self.comment.all().count()

    class Meta:
        ordering = ['-date_created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profiles')


    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.content}    {self.date_posted}"
    
    class Meta:
        ordering = ['-date_posted']
    
      


