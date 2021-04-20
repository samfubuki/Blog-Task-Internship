from django import forms
from .models import BlogDatabase

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogDatabase
        fields = ['blog_title','blog_description','blog_image']
        labels = {'blog_title':'Blog Title','blog_description':'Blog Description','profile_image':'Profile Image'}
        widgets = {
            'blog_title':forms.TextInput(attrs={'class':'form-control'}),
            'blog_description':forms.TextInput(attrs={'class':'form-control'}),
        }

    