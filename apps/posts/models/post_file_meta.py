from django.db import models
from .post import Post

class PostFileMeta(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='profile_pic_meta')
    post_file_meta_id=models.CharField(max_length=100,primary_key=True,default="")
    file_name=models.CharField(max_length=50,blank=True,null=True)
    file_url=models.CharField(max_length=100,blank=True,null=True)
    public_id=models.CharField(max_length=50,null=True,blank=True)
    resource_type=models.CharField(max_length=50,null=True,blank=True)
    types=models.CharField(max_length=50,null=True,blank=True)
    asset_id=models.CharField(max_length=50,null=True,blank=True)
    folder=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.CharField(max_length=50,null=True,blank=True)
    signature=models.CharField(max_length=50,null=True,blank=True)
    version_id=models.CharField(max_length=50,null=True,blank=True)
    version=models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        indexes=[
            models.Index(fields=['file_name'])
        ]

    def __str__(self) -> str:
        return f"{self.file_name} under {self.post.title}"