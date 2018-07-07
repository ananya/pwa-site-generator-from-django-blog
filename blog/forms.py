from django import forms

from .models import Post, Comment, PWA

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class PWAForm(forms.ModelForm):

    class Meta:
        model = PWA
        fields = ('name', 'short_name', 'start_url',)