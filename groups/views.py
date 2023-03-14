from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from groups.models import Group, GroupMember , GroupPost, GroupPostReaction
from groups.serializers import GroupSerializer, GroupPostSerializer, GroupPostReactionSerializer
from groups.permissions import IsGroupAdmin, IsGroupMember, IsGroupReadOnly

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsGroupAdmin)

    def get_queryset(self):
        return Group.objects.filter(group_members__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(group_admin=self.request.user)

class GroupPostViewSet(viewsets.ModelViewSet):
    queryset = GroupPost.objects.all()
    serializer_class = GroupPostSerializer
    permission_classes = (IsAuthenticated, IsGroupMember, IsGroupReadOnly)

    def get_queryset(self):
        return GroupPost.objects.filter(group__group_members__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GroupPostReactionViewSet(viewsets.ModelViewSet):
    queryset = GroupPostReaction.objects.all()
    serializer_class = GroupPostReactionSerializer
    permission_classes = (IsAuthenticated, IsGroupMember)

    def get_queryset(self):
        return GroupPostReaction.objects.filter(group_post__group__group_members__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)







# Create your views here.
