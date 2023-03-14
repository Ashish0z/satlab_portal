from rest_framework import serializers
from groups.models import Group, GroupMember , GroupPost, GroupPostReaction
import datetime
from django.contrib.auth import get_user_model

class GroupMemberSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    class Meta:
        model = GroupMember
        fields = (
            'user',
            'group'
        )


class GroupSerializer(serializers.ModelSerializer):
    group_members = GroupMemberSerializer(many=True, read_only=False)

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        group_members = validated_data.pop('group_members')
        group = Group.objects.create(**validated_data)
        for group_member in group_members:
            GroupMember.objects.create(group=group, **group_member)
            if (self.context['request'].user == group_member['user']):
                group.group_admin = group_member['user']
                group.save()
        return group



class GroupPostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=GroupMember.objects.all())
    post_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = GroupPost
        fields = '__all__'
        read_only_fields = (
            'user',
            'post_time'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['post_time'] = datetime.datetime.now()
        return GroupPost.objects.create(**validated_data)

class GroupPostReactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    reacton_date = serializers.DateTimeField(read_only=True)
    group_post = serializers.PrimaryKeyRelatedField(queryset=GroupPost.objects.all())
    
    class Meta:
        model = GroupPostReaction
        fields = '__all__'
        read_only_fields = (
            'user',
            'reacton_date'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['reacton_date'] = datetime.datetime.now()
        return GroupPostReaction.objects.create(**validated_data)
