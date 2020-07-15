from django.contrib.auth import get_user_model
from reat_framework import serializers
from core.models import Message, Profile, FriendRequest
from django.db.models import Q

# class FriendsFilter(serializers.PrimaryKeyRelatedField):
# 次はここから


class MessageSerializer(serializers.ModelSerializer):
    receiver = FriendsFilter()

    class Meta:
        model = Message
        fields = ('id', 'message', 'sender', 'receiver')
        extra_kwargs = {'sender': {'read_only': True}}
