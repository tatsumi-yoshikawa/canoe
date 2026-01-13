from django.urls import path
from app import views

urlpatterns = [
    path('base/', views.base, name='base'), 
    path('index/', views.index, name='index'), 
    path('detail/', views.detail, name='detail'), 
]
