from apps.posts.dto.deletePost.main import DeletePostDTO
from apps.posts.models.post import Post
from rest_framework import status

class DeletePostService:

    def __init__(self,dto:DeletePostDTO) -> None:
        self._dto=dto

    def delete(self,request:object)->tuple:
        try:
            _post=self._dto.post_id

            if request.User.username != _post.section.user.username:
                raise Exception("you can't delete this!")
            
            _post.delete()

            return (
                {"message":"deleted!"},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(e)