from django.urls import path
from apps.posts.controller.post_controller import PostController

urlpatterns = [
    path('',PostController.as_view())
]

