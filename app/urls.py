from django.urls import path
from app import views

# urlpatterns = [
#     path('base/', views.base, name='base'), 
#     path('index/', views.index, name='index'), 
#     path('detail/', views.detail, name='detail'), 
# ]


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    path('tweet/<int:pk>/like/', views.like_toggle, name='like_toggle'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
