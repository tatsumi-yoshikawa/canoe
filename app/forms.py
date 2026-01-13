from django import forms
from app.models import Tweet
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full bg-transparent border-none focus:ring-0 text-lg placeholder-gray-400 resize-none',
                'rows': 2,
                'placeholder': 'いまどうしてる？',
            })
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # 標準Userモデルにあるフィールドのみ使用
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded'}),
        }
