from rest_framework import serializers
from apps.auths.serializer.register.main import UserSerializer

class SharedPostSerializer(serializers.Serializer):
    share_id=serializers.CharField()
    from_user=UserSerializer()
    shared_at=serializers.DateTimeField()
