from tokenize import Comment
from rest_framework import serializers
from .models import Application, Post, Tag, Topic
from rest_framework.serializers import CurrentUserDefault


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'description')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'id', 'user_id', 'user', 'tags', 'content', 'topic',
            'created_at', 'updated_at'
        )
        read_only_fields = ('user_id', 'created_at', 'updated_at')

    def user_id(self, obj):
        return obj.user.id

    def tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'application_type', 'application_file')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            'id', 'user_id', 'user', 'post',
            'content', 'created_at', 'updated_at'
        )
        read_only_fields = ('user_id', 'created_at', 'updated_at')

    def user_id(self, obj):
        return obj.user.id
