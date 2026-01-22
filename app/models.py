# from django.db import models

# # Create your models here.

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# class User(AbstractBaseUser): 
#     """カスタムユーザーモデル"""

#     username = 
#     email = 
#     password = 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta: 
#         pass
    
#     def __str__(self):
#         return self.username





# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, name, password=None, **extra_fields):
#         """通常ユーザーを作成して保存する"""
#         if not email:
#             raise ValueError('メールアドレスは必須です')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password=None, **extra_fields):
#         """管理権限を持つユーザーを作成して保存する代"""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, name, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, verbose_name='メールアドレス')
#     name = models.CharField(max_length=255, verbose_name='名前')
#     profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='プロフィール画像')
#     bio = models.TextField(max_length=500, blank=True, verbose_name='自己紹介文')
    
#     # Djangoの管理画面や権限システムに必要
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     # ログイン時に使用するフィールドをメールアドレスに変更
#     USERNAME_FIELD = 'email'
#     # createsuperuserコマンドで入力を求められるフィールド（email, password以外）
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email



















# class Post(models.Model):
#     """投稿モデル"""
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     liked_users = models.ManyToManyField(User, through='GoodBad', through_fields=('post', 'user'))
#     title = models.CharField(max_length=200, help_text='タイトル')
#     content = models.TextField(blank=True, null=True, help_text='本文')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta: 
#         pass
    
#     def __str__(self):
#         return self.title


# class GoodBad(models.Model):
#     """グッドバッドモデル（中間テーブル）"""
    
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='goodbad')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goodbad')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         constraints = [models.UniqueConstraint(fields=['post', 'user'], name='unique_post_user')]
    
#     def __str__(self):
#         return f'{self.user.username} likes {self.post.title}'
