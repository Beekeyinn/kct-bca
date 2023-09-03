from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="post/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
