from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.translation import gettext, gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=250)
    cat_img = models.ImageField(upload_to='catimg', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title



class Post(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, related_name='cat', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = HTMLField()
    post_img = models.ImageField(upload_to='postimg', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name

class Comment(models.Model):
    users = models.ForeignKey(User, related_name='users', null=True, on_delete=models.CASCADE)
    client_allposts = models.ForeignKey(Post, related_name='client_allposts', null=True, on_delete=models.CASCADE)
    client_comment = models.TextField()
    send = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Commnent'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.client_comment} is made by {self.send}'

