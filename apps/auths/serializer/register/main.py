from rest_framework import serializers
from apps.auths.models.usermeta import UserMeta
from apps.auths.models.user import User

class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserMeta
        fields=('meta_id','profile_pic_url','doj')


class UserSerializer(serializers.ModelSerializer):
    user_meta=UserMetaSerializer()
    class Meta:
        model=User
        fields=('username','full_name','email','phone','user_meta')

#class RegisterSerializer(serializers.Serializer):
#    username=serializers.CharField()
#    full_name=serializers.CharField()
#    email=serializers.EmailField()
#    phone=serializers.CharField()
#
#class RegisterUserMetaSerializer(serializers.Serializer):
#    meta_id=serializers.CharField()
#    profile_pic_url=serializers.CharField()
#    doj=serializers.DateTimeField()
    