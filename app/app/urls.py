from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
import app.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
