from apps.auths.models.user import User
from apps.sections.models.section import Section
from datetime import datetime
from django.db import models
from apps.users.repository.getAllSharedSectionRepos.repo import GetAllSharedSectionRepo 

class SharedSection(models.Model):
    share_id=models.CharField(max_length=50,primary_key=True,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user_section')
    from_user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='from_user_section')
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    shared_at=models.DateTimeField(default=datetime.now())

    repo=GetAllSharedSectionRepo

    def __str__(self) -> str:
        return f"received from {self.from_user.full_name} to {self.user.full_name} section:{self.section.section_name}"