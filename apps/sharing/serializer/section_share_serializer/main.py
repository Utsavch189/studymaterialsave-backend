from rest_framework import serializers
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer
from apps.auths.serializer.register.main import UserSerializer

class SharedSectionSerializer(serializers.Serializer):
    share_id=serializers.CharField()
    from_user=UserSerializer()
    section=SectionReturnRespSerializer()
    shared_at=serializers.DateTimeField()
