from django.contrib import admin

# Register your models here.

from blog_app.models import Post, Like


class PostAdmin(admin.ModelAdmin): 
    # fields = []
    list_display = ['title', 'user', 'created_at', 'updated_at', ]
    list_filter = ['created_at', 'updated_at', ]
    search_fields = ['title', ]


class LikeAdmin(admin.ModelAdmin): 
    # fields = []
    list_display = ['user', 'post', 'created_at', ]
    list_filter = ['created_at', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
