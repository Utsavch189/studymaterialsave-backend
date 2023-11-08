from pydantic import BaseModel,validator,constr
from apps.posts.models.post import Post

class DeletePostDTO(BaseModel):
    post_id:constr(min_length=1,max_length=50,strip_whitespace=True)

    @validator('post_id',allow_reuse=True,always=True)
    def validate_post_id(cls,value):
        try:
            if not Post.objects.filter(post_id=value).exists():
                raise Exception("post id not found!")
            return Post.objects.get(post_id=value)
        except Exception as e:
            raise Exception(str(e))