from apps.sharing.models.sharedPosts import SharedPost
from rest_framework import status
from apps.sharing.dto.post_share_dto.addSharePostDto import AddSharePostDTO
from django.utils import timezone
from apps.sharing.serializer.post_share_serializer.main import SharedPostSerializer
import uuid
from datetime import datetime
from apps.posts.models.post import Post
from apps.posts.serializers.getPosts import PostSerializer
import json

class AddSharePostService:

    def __init__(self,dto:AddSharePostDTO) -> None:
        self._dto=dto
    
    def add(self,request:object)->tuple:
        try:
            _user=request.User

            if not _user.username==self._dto.post.section.user.username:
                raise Exception("you can not share this!")
            
            _shared_post=SharedPost(
                share_id=uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=str(datetime.now())),
                user=self._dto.user,
                from_user=_user,
                post=self._dto.post,
                shared_at=timezone.now()
            )
            _shared_post.save()

            _post=Post.repo().getAPost(post_id=self._dto.post.post_id)
            _post_data={"post":json.loads(json.dumps(PostSerializer(_post).data))}
            
            return (
                {"message":"successfully shared!","shared_data":{**SharedPostSerializer(_shared_post).data,**_post_data}},
                status.HTTP_202_ACCEPTED
            )

        except Exception as e:
            raise Exception(str(e))