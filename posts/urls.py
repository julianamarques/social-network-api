from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import ApiRoot, ImportDatabase, ProfileList, ProfileDetail, PostList, PostDetail, ProfilePostsList, PostCommentsList, CommentList

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('import-database/', ImportDatabase.as_view(), name=ImportDatabase.name),
    path('users/', ProfileList.as_view(), name=ProfileList.name),
    path('users/<int:id>/', ProfileDetail.as_view(), name=ProfileDetail.name),
    path('posts/', PostList.as_view(), name=PostList.name),
    path('posts/<int:id>/', PostDetail.as_view(), name=PostDetail.name),
    path('posts-comments/', PostCommentsList.as_view(), name=PostCommentsList.name),
    path('user-posts/', ProfilePostsList.as_view(), name=ProfilePostsList.name),
    path('comments/', CommentList.as_view(), name=CommentList.name),
    path('api-token-auth/', obtain_auth_token),
]