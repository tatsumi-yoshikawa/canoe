from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    # いいね機能 (多対多)
    likes = models.ManyToManyField(User, related_name="liked_tweets", blank=True)

    class Meta:
        ordering = ['-created_at']  # 最新順

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
