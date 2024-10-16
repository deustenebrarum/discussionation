from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet, TopicViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

router = DefaultRouter()

router.register(r'tags', TagViewSet, basename='tag')
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
#pip install djangorestframework-simplejwt
