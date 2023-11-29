from django.urls import path
from apps.posts.controller.post_controller import PostController,PostGetController
from apps.posts.controller.post_meta_controller import PostMetaController

urlpatterns = [
    path('',PostController.as_view()),
    path('section_id=<str:section_id>&post_id=<str:post_id>/',PostGetController.as_view()),
    path('post-meta',PostMetaController.as_view())
]

