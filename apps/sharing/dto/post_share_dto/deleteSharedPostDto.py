from pydantic import BaseModel,validator,constr
from apps.sharing.models.sharedPosts import SharedPost

class DeleteASharedPostDTO(BaseModel):
    share_id:constr(min_length=1,max_length=50,strip_whitespace=True)

    @validator('share_id',allow_reuse=True,always=True)
    def validate_share_id(cls,value):
        try:
            if SharedPost.objects.filter(share_id=value).exists():
                return SharedPost.objects.get(share_id=value)
            else:
                raise Exception('user not found!')
        except Exception as e:
            raise Exception(str(e))
