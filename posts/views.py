from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import Post, Comment, Profile
from .serializers import ProfileSerializer, ProfilePostSerializer, PostSerializer, CommentSerializer, PostCommentsSerializer
from .permissions import OwnerOrReadOnly

import json


class ImportDatabase(generics.GenericAPIView):
    name = 'import-database'

    def get(self, request, *args, **kwargs):
        try:
            self.import_database()
            
            return Response({'Message' : 'Dados importados com sucesso!'}, status=status.HTTP_200_OK)

        except Exception:
            return Response({'Message' : 'Erro ao importar base de dados!'}, status=status.HTTP_400_BAD_REQUEST)

    def import_database(self):
        file = open('db.json')
        content = json.load(file)

        for profile in content['users']:
            Profile.objects.create(name=profile['name'], website=profile['website'], username=profile['username'], email=profile['email'])

        for post in content['posts']:
            profile = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'], body=post['body'], owner=profile)

        for comment in content['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(id=comment['id'], name=comment['name'], email=comment['email'], body=comment['body'], post=post)


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveAPIView):
    name = 'profile-detail'
    permission_classes = permissions.IsAuthenticated

    def get(self, request, id):
        try:
            profile = Profile.objects.get(id=id)
            serializer_class = ProfileSerializer(profile)
            return Response(data=serializer_class.data, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            return Response({'Message' : 'Perfil não encontrado!'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request,id):
        profile = Profile.objects.get(id=id)
        profile.delete()

        return Response({'Message', 'Usuário excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (OwnerOrReadOnly, permissions.IsAuthenticated)

class PostDetail(generics.RetrieveAPIView):
    name = 'post-detail'
    permission_classes = (OwnerOrReadOnly, permissions.IsAuthenticated)
    
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer_class = PostSerializer(post)
            return Response(data=serializer_class.data,status=status.HTTP_200_OK)

        except Post.DoesNotExist:
            return Response({'Message' : 'Post não encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request,id):
        post = Post.objects.get(id=id)
        post.delete()

        return Response({'Message' : 'Post excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class ProfilePostsList(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name='profile-posts'


class PostCommentsList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class = PostCommentsSerializer
    name='posts-comments'


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response({
            "import-database" : reverse(ImportDatabase.name, request=request),
            "posts" : reverse(PostList.name, request=request),
            "profiles" : reverse(ProfileList.name, request=request),
            "posts-comments" : reverse(PostCommentsList.name, request=request),
            "profile-posts" : reverse(ProfilePostsList.name, request=request)
        })
