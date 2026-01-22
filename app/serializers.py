# from django.contrib.auth.models import User, Group
# from blog_app.models import Post, Like
# from rest_framework import serializers


# # class GroupSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Group
# #         fields = ['url', 'name', ]


# # class PostSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Post
# #         fields = ['url', 'user', 'liked_users', 'title', 'content', 'created_at', 'updated_at', ]


# # class LikeSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Like
# #         fields = ['url', 'post', 'user', 'created_at', ]


# # class UserSerializer(serializers.HyperlinkedModelSerializer): 
# #     # 「いいねした記事」を直接取得したい場合 SerializerMethodField を使ってカスタマイズするのが一般的
# #     posts = PostSerializer(many=True, read_only=True)
# #     liked_posts = serializers.SerializerMethodField()

# #     class Meta: 
# #         model = User
# #         fields = ['url', 'username', 'email', 'password', 'date_joined', 'posts', 'liked_posts', ]

# #     def get_liked_posts(self, obj): 
# #         # obj は User インスタンス
# #         # Like テーブルを通じて Post を取得
# #         liked_posts = Post.objects.filter(likes__user=obj)
# #         # 親が持っている request 情報を context として子に引き継ぐ
# #         return PostSerializer(liked_posts, many=True, context=self.context).data


# # 以下は HyperlinkedModelSerializer ではなく、ModelSerializer を使用
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id', 'name', ]


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = ['id', 'post', 'user', 'created_at', ]


# class AuthorSerializer(serializers.ModelSerializer): 
#     # 筆者表示用の軽量シリアライザ
#     class Meta: 
#         model = User
#         fields = ['id', 'username', ]


# class PostSerializer(serializers.ModelSerializer): 
#     # user フィールドを上書きする
#     user = AuthorSerializer(read_only=True)
#     # views.py の annotate で追加したフィールドを定義
#     # default=0 を設定することで、annotate が漏れた場合でも API が0を返す
#     likes_count = serializers.IntegerField(read_only=True, default=0)

#     class Meta: 
#         model = Post
#         # fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user', 'liked_users', ]
#         fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user', 'likes_count', ]
#         # read_only_fields = ['user', ]


# class UserSerializer(serializers.ModelSerializer): 
#     # 「いいねした記事」を直接取得したい場合 SerializerMethodField を使ってカスタマイズするのが一般的
#     posts = PostSerializer(many=True, read_only=True)
#     liked_posts = serializers.SerializerMethodField()

#     class Meta: 
#         model = User
#         fields = ['id', 'username', 'email', 'password', 'date_joined', 'posts', 'liked_posts', ]
#         # パスワードは書き込み専用
#         extra_kwargs = {'password': {'write_only': True, }, }

#     def get_liked_posts(self, obj): 
#         # obj は User インスタンス
#         # Like テーブルを通じて Post を取得
#         liked_posts = Post.objects.filter(likes__user=obj)
#         # 親が持っている request 情報を context として子に引き継ぐ
#         return PostSerializer(liked_posts, many=True, context=self.context).data

#     def create(self, validated_data): 
#         # 作成時は UserManager の create_user を使うと安全
#         # パスワードのハッシュ化も自動で行われる
#         return User.objects.create_user(**validated_data)

#     def update(self, instance, validated_data): 
#         # パスワードを validated_data から取り出す（popする）
#         password = validated_data.pop('password', None)

#         # その他のフィールドを更新
#         instance = super().update(instance, validated_data)

#         # パスワードが存在する場合のみ set_password() でハッシュ化して保存
#         if password: 
#             instance.set_password(password)
#             instance.save()

#         return instance
