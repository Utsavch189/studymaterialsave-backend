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
    
    def modify(self)->tuple:
        try:
            post=Post.objects.get(post_id=self._dto.post_id)
            post.title=self._dto.title
            post.about=self._dto.about
            post.notes=self._dto.notes
            post.save()

            _updated_data=self._getAPost(self._dto.post_id)

            return (
                {"message":"updated!","post":json.loads(json.dumps(PostSerializer(_updated_data).data))},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(str(e))