from pydantic import BaseModel,validator,constr
from apps.posts.models.post import Post

VISIBILITY=['PUBLIC','PRIVATE']

class ModifyPostDTO(BaseModel):
    post_id:constr(min_length=1,max_length=50,strip_whitespace=True)
    title:constr(min_length=1,max_length=50,strip_whitespace=True)
    about:constr(min_length=1,max_length=150,strip_whitespace=True)
    visibility:constr(max_length=10,strip_whitespace=True)
    notes:constr(min_length=1,strip_whitespace=True)

    @validator('post_id',allow_reuse=True,always=True)
    def validate_post_id(cls,value):
        try:
            if not Post.objects.filter(post_id=value).exists():
                raise Exception("post id not found!")
            return Post.objects.get(post_id=value)
        except Exception as e:
            raise Exception(str(e))
    
    @validator('title',allow_reuse=True,always=True)
    def title_validate(cls,value,values):
        try:
            if Post.objects.get(post_id=values['post_id']).title!=value:
                if not Post.objects.filter(title=value).exists():
                    return value
                else:
                    raise Exception("already same title exists..")
            else:
                return value
        except Exception as e:
            raise Exception(str(e))
    
    @validator('visibility',allow_reuse=True,always=True)
    def visibility_validate(cls,value):
        if not value.upper() in VISIBILITY:
            raise Exception('visibility should be either public or private!')
        return value.upper()