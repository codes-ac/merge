from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    content = models.TextField()
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=140)
    image = models.ImageField(default="deafult.png", upload_to="blog/images", blank=True)


    def __str__(self):
        return f"Blog of {self.author}"


class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] +"... by "+ self.user.username
    
    