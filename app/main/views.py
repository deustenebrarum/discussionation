import rest_framework.permissions
from .models import Post, Tag, Topic
from .serializers import PostSerializer, TagSerializer, TopicSerializer
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class TopicViewSet(ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = [IsAdminUser]


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
