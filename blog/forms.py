# define own form PostForm according to Post data model,specify which field should be displayed for the form

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text')