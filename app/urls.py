from django.urls import path
from app import views

# urlpatterns = [
#     path('base/', views.base, name='base'), 
#     path('index/', views.index, name='index'), 
#     path('detail/', views.detail, name='detail'), 
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('tweet/<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
]
