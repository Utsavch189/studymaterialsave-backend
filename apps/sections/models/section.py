from django.db import models
from apps.auths.models.user import User
from datetime import datetime
from apps.sections.repository.section_model.repo import SectionModelRepo

class Section(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sections')
    section_id=models.CharField(max_length=50,primary_key=True,default="")
    section_name=models.CharField(max_length=100,null=True,blank=True)
    section_about=models.CharField(max_length=150,null=True,blank=True)
    visibility=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())

    repo=SectionModelRepo

    class Meta:
        indexes=[
            models.Index(fields=['section_name'])
        ]

    def __str__(self) -> str:
        return f"{self.section_name} created by {self.user.full_name}"