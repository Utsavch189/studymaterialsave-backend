from rest_framework import serializers
from apps.auths.serializer.register.main import UserSerializer
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer
from apps.posts.serializers.getPosts import PostSerializer

class SharedSectionDataSerializer(serializers.Serializer):
    share_id=serializers.CharField()
    from_user=UserSerializer()
    section=SectionReturnRespSerializer()
    shared_at=serializers.DateTimeField()


class SharedPostDataSerializer(serializers.Serializer):
    share_id=serializers.CharField()
    from_user=UserSerializer()
    post=PostSerializer()
    shared_at=serializers.DateTimeField()