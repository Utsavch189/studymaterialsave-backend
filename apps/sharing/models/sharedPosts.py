from apps.auths.models.user import User
from apps.posts.models.post import Post
from django.db import models
from datetime import datetime
from apps.users.repository.getAllSharedPostRepo.repo import GetAllSharedPostRepo

class SharedPost(models.Model):
    share_id=models.CharField(max_length=50,primary_key=True,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user_post')
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user_post')
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    shared_at=models.DateTimeField(default=datetime.now())

    repo=GetAllSharedPostRepo


    def __str__(self) -> str:
        return f"received from {self.from_user.full_name} to {self.user.full_name} post:{self.post.title}"