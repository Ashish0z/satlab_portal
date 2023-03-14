from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(defaults={'username': 'deleted2', 'password': 'deleted'})[0]

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    group_description = models.TextField()
    group_members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='GroupMember')
    is_read_only = models.BooleanField(default=False)
    group_admin = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.SET(get_sentinel_user),
    related_name='group_admin',
    default=1)

    def __str__(self):
        return self.group_name

class GroupMember(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))

class GroupPost(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    post = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.post

class GroupPostReaction(models.Model):

    group_post = models.ForeignKey('GroupPost', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reacton_date = models.DateTimeField(auto_now_add=True)
    reaction = models.CharField(max_length=1, default='like', choices=(
        ('0', 'like'),
        ('1', 'dislike'),
        ('2', 'love'),
        ('3', 'haha'),
        ('4', 'wow'),
        ('5', 'sad'),
        ('6', 'angry'),
    ))

    def __str__(self):
        return self.user.username
