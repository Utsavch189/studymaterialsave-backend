from apps.posts.dto.deletePost.main import DeletePostDTO
from apps.posts.models.post import Post
from rest_framework import status

class DeletePostService:

    def __init__(self,dto:DeletePostDTO) -> None:
        self._dto=dto

    def delete(self)->tuple:
        try:
            Post.objects.get(post_id=self._dto.post_id).delete()
            return (
                {"message":"deleted!"},
                status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            raise Exception(e)