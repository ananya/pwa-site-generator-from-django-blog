from django.db import models
from django.utils import timezone

class PWA(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    start_url = models.CharField(max_length=200, default='/')
    
    icon_src_1 = models.CharField(max_length=200, default='add link to image')
    size_1 = models.CharField(max_length=200, default='128x128')
    type_of_icon_1 = models.CharField(max_length=200, default='image/png') 
    
    icon_src_2 = models.CharField(max_length=200, default='add link to image')
    size_2 = models.CharField(max_length=200, default='144x144')
    type_of_icon_2 = models.CharField(max_length=200, default='image/png') 
    
    icon_src_3 = models.CharField(max_length=200, default='add link to image')
    size_3 = models.CharField(max_length=200, default='152x152')
    type_of_icon_3 = models.CharField(max_length=200, default='image/png') 
    
    icon_src_4 = models.CharField(max_length=200, default='add link to image')
    size_4 = models.CharField(max_length=200, default='192x192')
    type_of_icon_4 = models.CharField(max_length=200, default='image/png') 
    
    icon_src_5 = models.CharField(max_length=200, default='add link to image')
    size_5 = models.CharField(max_length=200, default='256x256')
    type_of_icon_5 = models.CharField(max_length=200, default='image/png') 
    
    icon_src_6 = models.CharField(max_length=200, default='add link to image')
    size_6 = models.CharField(max_length=200, default='512x512')
    type_of_icon_6 = models.CharField(max_length=200, default='image/png') 
    
    display = models.CharField(max_length=200, default='standalon') 
    background_color = models.CharField(max_length=200, default='#3E4EB8') 
    theme_color = models.CharField(max_length=200, default='#2F3BA2') 


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

