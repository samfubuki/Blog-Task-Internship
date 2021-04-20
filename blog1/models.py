from django.db import models
# Create your models here.

class BlogDatabase(models.Model):
    blog_title = models.CharField(max_length=1000)
    blog_description = models.CharField(max_length=10000)
    blog_image=models.ImageField(upload_to='profileimg',blank=True)
