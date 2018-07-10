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
        fields = ('name', 'short_name', 'start_url', 'icon_src_1', 'size_1', 'type_of_icon_1', 'icon_src_2', 'size_2', 'type_of_icon_2', 'icon_src_3', 'size_3', 'type_of_icon_3', 'icon_src_4', 'size_4', 'type_of_icon_4', 'icon_src_5', 'size_5', 'type_of_icon_5', 'icon_src_6', 'size_6', 'type_of_icon_6', 'display', 'background_color', 'theme_color')
