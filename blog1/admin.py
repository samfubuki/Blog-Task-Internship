from django.contrib import admin
from . models import BlogDatabase
# Register your models here.

@admin.register(BlogDatabase)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','blog_title','blog_description','blog_image']