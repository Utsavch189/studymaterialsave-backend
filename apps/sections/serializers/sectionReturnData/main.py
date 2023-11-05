from rest_framework import serializers

class SectionReturnRespSerializer(serializers.Serializer):
    section_id=serializers.CharField()
    section_name=serializers.CharField()
    section_about=serializers.CharField()
    visibility=serializers.CharField()
    created_at=serializers.DateTimeField()