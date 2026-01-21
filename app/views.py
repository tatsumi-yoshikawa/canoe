from django.shortcuts import render

# Create your views here.


# Postscript

def base(request): 
    return render(request, 'app/base.html')


def index(request): 
    return render(request, 'app/index.html')


def detail(request): 
    return render(request, 'app/detail.html')










from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.db.models import Count, Value
from django.db.models.functions import Coalesce
from blog_app.models import Post, Like
from blog_app.serializers import UserSerializer, GroupSerializer, PostSerializer, LikeSerializer
from blog_app.permissions import IsOwnerOrCreateRead, IsOwnerOrAuthenticatedCreateReadOrReadOnly
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


def index(request):
    return HttpResponse('Hello, world. You are at the index page.')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined').prefetch_related('posts', 'likes__post')
    serializer_class = UserSerializer
    # permission_classes = [IsOwnerOrCreateRead]
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows likes to be viewed or edited.
    """

    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    # likes__user を prefetch すれば、likes モデルに属する created_at フィールドは自動的に取得されます
    # queryset = Post.objects.all().order_by('-created_at').select_related('user').prefetch_related('likes__user')
    # ルーターやスキーマ生成のために追加
    # get_queryset が定義されていれば、実際のデータ取得にはそちらが使われる
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrAuthenticatedCreateReadOrReadOnly]

    # detail=True は単一の Post に対してのアクションであることを示す
    # methods=['post'] で POST リクエストのみ受け付ける
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None): 
        post = self.get_object()
        user = request.user

        # いいねの存在確認
        # Django ビューで get_or_create() を使用する際の注意点
        # よほどの理由がない限り、 POST リクエスト以外では使用しない
        obj, created = Like.objects.get_or_create(user=user, post=post)

        if not created: 
            # 既に存在していた場合は削除
            obj.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else: 
            # そうでない場合は新規作成
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer): 
        # 保存時にログイン中のユーザーを user として渡す
        serializer.save(user=self.request.user)

    def get_queryset(self): 
        # Coalesce で、もし Count が None を返したとしても Value(0) に置き換えられる
        queryset = Post.objects.all().select_related('user').annotate(
            likes_count=Coalesce(Count('liked_users', distinct=True), Value(0))
        ).order_by('-created_at')

        # もし「『いいね』したユーザの数」ではなく「ユーザの情報そのもの」を出すなら追加
        # queryset = queryset.prefetch_related('likes__user')

        return queryset
