from pydantic import BaseModel,validator,constr
from apps.posts.models.post import Post
from apps.sections.models.section import Section

class GetPostDTO(BaseModel):
    section_id:constr(max_length=50,strip_whitespace=True)="None"
    post_id:constr(max_length=50,strip_whitespace=True)="None"

    @validator('post_id',allow_reuse=True,always=True)
    def validate_post_id(cls,value):
        try:
            if value!="None":
                if not Post.objects.filter(post_id=value).exists():
                    raise Exception("post id is invalid!")
                return value
            return None
        except Exception as e:
            raise Exception(str(e))
    
    @validator('section_id',allow_reuse=True,always=True)
    def validate_id(cls,value):
        try:
                if value!="None":
                    if Section.objects.filter(section_id=value).exists():
                        return value
                    else:
                        raise Exception("section is not found!")
                return None
        except Exception as e:
            raise Exception(str(e))
