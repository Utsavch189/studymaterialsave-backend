from django.contrib import admin
from apps.posts.models.post import Post
from apps.posts.models.post_file_meta import PostFileMeta

admin.site.register(Post)
admin.site.register(PostFileMeta)
