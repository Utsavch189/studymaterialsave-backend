from rest_framework import serializers
from apps.auths.serializer.register.main import UserSerializer
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer

class SharedSectionDataSerializer(serializers.Serializer):
    share_id=serializers.CharField()
    from_user=UserSerializer()
    section=SectionReturnRespSerializer()
    shared_at=serializers.DateTimeField()