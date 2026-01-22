# from rest_framework import permissions


# # class BlocklistPermission(permissions.BasePermission):
# #     """
# #     Global permission check for blocked IPs.
# #     """

# #     def has_permission(self, request, view):
# #         ip_addr = request.META['REMOTE_ADDR']
# #         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
# #         return not blocked


# # class IsOwnerOrReadOnly(permissions.BasePermission):
# #     """
# #     Object-level permission to only allow owners of an object to edit it.
# #     Assumes the model instance has an `owner` attribute.
# #     オブジェクトの所有者（owner）だけが編集・削除を許可され、
# #     それ以外の人は閲覧（GET）のみ許可されるカスタム権限
# #     """

# #     def has_object_permission(self, request, view, obj):
# #         # Read permissions are allowed to any request,
# #         # so we'll always allow GET, HEAD or OPTIONS requests.
# #         # SAFE_METHODS（GET, HEAD, OPTIONS）リクエストは常に許可する
# #         if request.method in permissions.SAFE_METHODS:
# #             return True

# #         # Instance must have an attribute named `owner`.
# #         # PUT, DELETE などの書き込みリクエストは、
# #         # オブジェクトの所有者とリクエストユーザーが一致する場合のみ許可する
# #         # モデルのフィールド名が 'owner' であると仮定
# #         return obj.owner == request.user


# class IsOwnerOrCreateRead(permissions.BasePermission):
#     """
#     For User Model
#     unauthenticated user: GET, POST
#     authenticated user: GET, POST
#     owner: All
#     """

#     def has_permission(self, request, view):
#         # has_permission で False が返った場合、has_object_permission は呼ばれない
#         # True が返った場合、データベースがたたかれ当該オブジェクトが取得され、
#         # そのうえで has_object_permission が実行される
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         if request.method == 'POST':
#             return True
        
#         # 無駄にデータベースをたたかないため
#         # より適切なエラーコードを返すため
#         return request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         # POST リクエストの場合はこの関数は実行されない
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.username == request.user


# class IsOwnerOrAuthenticatedCreateReadOrReadOnly(permissions.BasePermission):
#     """
#     For Post Model
#     unauthenticated user: GET
#     authenticated user: GET, POST
#     owner: All
#     """

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         return request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return obj.user == request.user
