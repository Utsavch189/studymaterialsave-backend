from rest_framework import serializers

class PostMetaSerializer(serializers.Serializer):
    post_file_meta_id=serializers.CharField()
    file_name=serializers.CharField()
    file_url=serializers.CharField()
    public_id=serializers.CharField()
    resource_type=serializers.CharField()
    types=serializers.CharField()

class PostSerializer(serializers.Serializer):
    post_id=serializers.CharField()
    title=serializers.CharField()
    about=serializers.CharField()
    notes=serializers.CharField()
    created_at=serializers.DateTimeField()
    post_meta=PostMetaSerializer(many=True)