from rest_framework import serializers
from .models import Post, Profile, Comment


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'username', 'website']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'name', 'body', 'post']


class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'website', 'posts']


class PostCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'owner', 'comments']
