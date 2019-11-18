from django.db import models


class Profile(models.Model):
    user = models.ForeignKey('auth.User', related_name='profiles', on_delete = models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    class Meta:
        db_table = 'profile'


    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'


    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=75)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'
