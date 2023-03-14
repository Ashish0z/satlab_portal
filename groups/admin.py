from django.contrib import admin
from .models import Group, GroupMember, GroupPost, GroupPostReaction

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupPost)
admin.site.register(GroupPostReaction)

# Register your models here.
