from django.contrib import admin

from .models import (
    Application, Post, Comment,
    Topic, Tag
)

admin.site.register(Application)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'topic', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'topic')
    search_fields = ('user__username', 'content', 'topic__title', 'tags__title')
    list_filter = ('topic', 'tags', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Tag)
