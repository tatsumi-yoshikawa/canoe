from django.shortcuts import render

# Create your views here.


# Postscript

# def base(request): 
#     return render(request, 'app/base.html')


# def index(request): 
#     return render(request, 'app/index.html')


# def detail(request): 
#     return render(request, 'app/detail.html')


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from app.models import Tweet
from app.forms import TweetForm

def index(request):
    tweets = Tweet.objects.order_by('-created_at')
    form = TweetForm()
    return render(request, 'app/index.html', {'tweets': tweets, 'form': form})

def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save()
            # HTMXリクエストに対しては、作成されたツイートのHTML断片だけを返す
            return render(request, 'app/partials/tweet.html', {'tweet': tweet})
    return HttpResponse(status=400)

def like_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        tweet.likes += 1
        tweet.save()
        # いいねボタン部分だけを更新するために、ボタンのHTML断片を返す
        return render(request, 'app/partials/like_button.html', {'tweet': tweet})
    return HttpResponse(status=400)
