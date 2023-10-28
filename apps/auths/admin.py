from django.contrib import admin
from .models.user import User
from .models.usermeta import UserMeta
from .models.profile_pic_meta import ProfilePicMeta

admin.site.register(User)
admin.site.register(UserMeta)
admin.site.register(ProfilePicMeta)