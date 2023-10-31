from django.urls import path
from apps.posts.controller.post_controller import PostController
from apps.posts.controller.post_meta_controller import PostMetaController

urlpatterns = [
    path('',PostController.as_view()),
    path('post-meta',PostMetaController.as_view())
]

