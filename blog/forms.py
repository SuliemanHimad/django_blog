from django import forms
from .models import Category, Post
from django.db.models import fields
from django.forms import widgets

class CategoryModalForm(forms.ModelForm):
    class Meta:
        model = Category  
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
        }


class PostModalForm(forms.ModelForm):
    class Meta:
        model=Post
        fields =['title','slug','category','image','content','published','tags']