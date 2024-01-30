from django.contrib import admin
from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'body']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'text', 'publish']
    list_filter = ['publish', 'author']
    search_fields = ['title', 'text']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['publish']
