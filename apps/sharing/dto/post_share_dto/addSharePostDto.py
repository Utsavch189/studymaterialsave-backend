from pydantic import BaseModel,validator,constr
from apps.posts.models.post import Post
from apps.auths.models.user import User

class AddSharePostDTO(BaseModel):
    user:constr(min_length=1,max_length=50,strip_whitespace=True) # take id
    post:constr(min_length=1,max_length=50,strip_whitespace=True) # take id

    @validator('user',allow_reuse=True,always=True)
    def validate_user(cls,value):
        try:
            if User.objects.filter(username=value).exists():
                return User.objects.get(username=value)
            else:
                raise Exception('user not found!')
        except Exception as e:
            raise Exception(str(e))
    
    @validator('post',allow_reuse=True,always=True)
    def validate_section(cls,value):
        try:
            if Post.objects.filter(post_id=value).exists():
                return Post.objects.get(post_id=value)
            else:
                raise Exception('post not found!')
        except Exception as e:
            raise Exception(str(e))
