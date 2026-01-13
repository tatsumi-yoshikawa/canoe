from django.shortcuts import render

# Create your views here.


# Postscript

# def base(request): 
#     return render(request, 'app/base.html')


# def index(request): 
#     return render(request, 'app/index.html')


# def detail(request): 
#     return render(request, 'app/detail.html')


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from app.models import Tweet
from app.forms import TweetForm, UserUpdateForm


@login_required
def timeline(request):
    # Userモデルのみ結合（Profile結合は削除）
    tweets = Tweet.objects.select_related('user').prefetch_related('likes')
    form = TweetForm()
    return render(request, 'app/timeline.html', {
        'tweets': tweets,
        'form': form
    })


@login_required
@require_http_methods(["POST"])
def tweet_create(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return render(request, 'app/partials/tweet.html', {'tweet': tweet})
    return render(request, 'app/partials/tweet.html', {'error': True}) # 簡易エラー処理


@login_required
@require_http_methods(["POST"])
def like_toggle(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    user = request.user
    
    if user in tweet.likes.all():
        tweet.likes.remove(user)
        is_liked = False
    else:
        tweet.likes.add(user)
        is_liked = True
        
    return render(request, 'app/partials/like_button.html', {
        'tweet': tweet,
        'is_liked': is_liked
    })


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('timeline')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'app/profile_edit.html', {'form': form})
