from apps.posts.models.post import Post
from apps.posts.dto.getPost.main import GetPostDTO
from typing import List
from apps.posts.dataContainers.main import PostData
from rest_framework import status
from apps.posts.serializers.getPosts import PostSerializer
import json

class GetPostService:

    def __init__(self,dto:GetPostDTO) -> None:
        self._dto=dto
    
    def _getAllPosts(self,section_id:str)->List[PostData]:
        return Post.repo().getAllPostsOfASection(section_id)
    
    def _getAPost(self,post_id:str)->PostData:
        return Post.repo().getAPost(post_id=post_id)

    def get(self)->tuple:
        try:
            if self._dto.post_id:
                _result=self._getAPost(post_id=self._dto.post_id)
                _data=json.loads(json.dumps(PostSerializer(_result).data))
            else:
                _result=self._getAllPosts(section_id=self._dto.section_id)
                _data=json.loads(json.dumps(PostSerializer(_result,many=True).data))

            return (
                {"message":"post fetched!","post":_data},
                status.HTTP_200_OK
            )
        except Exception as e:
            raise Exception(str(e))