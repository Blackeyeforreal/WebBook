from django.db import models
from django.contrib.auth.models import User
def content_file_name(instance, filename):
    return '/'.join(['docx', instance.Name,  filename])
def content_img_name(instance, filename):
    return '/'.join(['docx', instance.Name,  instance.name])

class Document(models.Model):
    duser = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    Name = models.CharField(max_length=255, blank=True )
    document = models.FileField(upload_to=content_file_name)
    summary = models.TextField(max_length=500, blank=True)
    img = models.ImageField(default="default.jpg",upload_to="img")

    uploaded_at = models.DateTimeField(auto_now_add=True)

class pdfDocument(models.Model):

    Name = models.CharField(max_length=255, blank=True )
    document = models.FileField(upload_to=content_file_name)
    uploaded_at = models.DateTimeField(auto_now_add=True)



