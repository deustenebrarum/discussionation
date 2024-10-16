from .models import Application, Post, Tag, Topic, Comment
from .serializers import (
    ApplicationSerializer, CommentSerializer, PostSerializer,
    TagSerializer, TopicSerializer
)
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticatedOrReadOnly
)


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TopicViewSet(ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
