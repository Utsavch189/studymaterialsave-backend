from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    full_name=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()

class RegisterUserMetaSerializer(serializers.Serializer):
    meta_id=serializers.CharField()
    profile_pic_url=serializers.CharField()
    doj=serializers.DateTimeField()
    