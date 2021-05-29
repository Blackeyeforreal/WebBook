from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class posts(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    psub= models.CharField(max_length=255)
    pdes = models.TextField(max_length=255)
    ptags = models.CharField(max_length=255)
    bku = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="bookmark")


class post(models.Model):
    post = models.ForeignKey(posts,default=1, on_delete=models.CASCADE)
    pcomment = models.TextField(max_length=255, default=3)
    likes = models.ImageField(max_length=255, default=4)




class book_reck(models.Model):
    buser = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    bname = models.CharField(max_length=100)
    bdes = models.TextField(max_length=355)
    bid = models.ImageField(max_length=311, default="default_book.jpg")


