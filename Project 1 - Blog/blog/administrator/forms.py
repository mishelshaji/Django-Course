from django import forms
from django.forms import widgets
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '3'}
            ),
            'color': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'color'}
            ),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'slug': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '3'}
            ),
            'featured_image': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
            'category': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'body': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
            'published_on': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'status': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }