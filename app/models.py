from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser): 
    """カスタムユーザーモデル"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        pass
    
    def __str__(self):
        return self.username


class Post(models.Model):
    """投稿モデル"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    liked_users = models.ManyToManyField(User, through='Like', through_fields=('post', 'user'))
    title = models.CharField(max_length=200, help_text='タイトル')
    content = models.TextField(blank=True, null=True, help_text='本文')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        pass
    
    def __str__(self):
        return self.title


class GoodBad(models.Model):
    """グッドバッドモデル（中間テーブル）"""
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['post', 'user'], name='unique_post_user')]
    
    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
