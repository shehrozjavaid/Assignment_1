from django.db import models

# Create your models here.

class blogpost(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_body = models.CharField(max_length=3000)
    blog_author = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_title