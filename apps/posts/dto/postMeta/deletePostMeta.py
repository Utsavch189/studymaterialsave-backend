from pydantic import BaseModel,validator,constr
from apps.posts.models.post_file_meta import PostFileMeta
from apps.posts.models.post import Post

class DeletePostMetaDTO(BaseModel):
    post_meta_id:constr(min_length=1,max_length=50,strip_whitespace=True)
    post_id:constr(min_length=1,max_length=50,strip_whitespace=True)

    @validator('post_id',allow_reuse=True,always=True)
    def validate_post_id(cls,value):
        try:
            if not Post.objects.filter(post_id=value).exists():
                raise Exception("post id not found!")
            return value
        except Exception as e:
            raise Exception(str(e))

    @validator('post_meta_id',allow_reuse=True,always=True)
    def validate_postMetaId(cls,value):
        try:
            if PostFileMeta.objects.filter(post_meta_id=value).exists():
                return value
            else:
                raise Exception("post meta id is not found!")
        except Exception as e:
            raise Exception(str(e))