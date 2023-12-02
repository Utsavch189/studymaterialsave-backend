from apps.posts.dto.modifyPost.main import ModifyPostDTO
from apps.posts.models.post import Post
from rest_framework import status
from apps.posts.serializers.getPosts import PostSerializer
from apps.posts.dataContainers.main import PostData
import json

class ModifyPostService:

    def __init__(self,dto:ModifyPostDTO) -> None:
        self._dto=dto
    
    def _getAPost(self,post_id:str)->PostData:
        return Post.repo().getAPost(post_id=post_id)
    
    def modify(self,request:object)->tuple:
        try:
            _post=self._dto.post_id

            if request.User.username != _post.section.user.username:
                raise Exception("you can't modify this!")

            print(_post)

            _post.title=self._dto.title
            _post.about=self._dto.about
            _post.notes=self._dto.notes
            _post.visibility=self._dto.visibility
            _post.save()

            _updated_data=self._getAPost(_post.post_id)

            return (
                {"message":"updated!","post":json.loads(json.dumps(PostSerializer(_updated_data).data))},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(str(e))