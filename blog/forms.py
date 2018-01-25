# define own form PostForm according to Post data model,specify which field should be displayed for the form

from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')