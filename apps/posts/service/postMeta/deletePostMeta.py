from apps.posts.dto.postMeta.deletePostMeta import DeletePostMetaDTO
from apps.posts.models.post_file_meta import PostFileMeta
from apps.posts.models.post import Post
from apps.posts.serializers.getPosts import PostSerializer
from rest_framework import status
from apps.posts.dataContainers.main import PostData
import json

class DeletePostMetaService:

    def __init__(self,dto:DeletePostMetaDTO) -> None:
        self._dto=dto

    def _getAPost(self,post_id)->PostData:
        return Post.repo().getAPost(post_id=post_id)
    
    def delete(self)->tuple:
        try:
            PostFileMeta.objects.get(post_file_id=self._dto.post_meta_id).delete()
            _post=self._getAPost(post_id=self._dto.post_id)
            return (
                {"message":"deleted!","post":json.loads(json.dumps(PostSerializer(_post).data))},
                status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            raise Exception(str(e))