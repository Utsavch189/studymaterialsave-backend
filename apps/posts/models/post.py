from django.db import models
from datetime import datetime
from apps.sections.models.section import Section
from apps.posts.repository.post_model.repo import PostModelRepo

class Post(models.Model):
    section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name='section')
    post_id=models.CharField(max_length=50,primary_key=True,default="")
    title=models.CharField(max_length=50,blank=True,null=True)
    about=models.CharField(max_length=150,blank=True,null=True)
    notes=models.TextField()
    visibility=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())

    repo=PostModelRepo

    class Meta:
        indexes=[
            models.Index(fields=['title'])
        ]

    def __str__(self) -> str:
        return f"{self.title} under {self.section.section_name}"