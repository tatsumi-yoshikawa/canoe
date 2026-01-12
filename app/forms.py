from django import forms
from app.models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full bg-gray-100 rounded-lg p-4 border border-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:bg-white transition duration-200 resize-none',
                'rows': '3',
                'placeholder': '今どうしてる？',
                # Alpine.jsと連携するための属性
                'x-model': 'content', 
                'maxlength': '280'
            })
        }
