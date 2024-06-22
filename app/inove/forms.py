# inove/forms.py

from django import forms
from .models_sqlalchemy import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'user_id']
        widgets = {
            'user_id': forms.Select
        }
