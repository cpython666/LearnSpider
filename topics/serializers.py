from rest_framework import serializers
from .models import Topics
class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        response_path = representation.get('response_path')
        api_prefix = representation.get('api_prefix')
        if response_path:
            representation['response_path'] = f"{api_prefix}{response_path}"
        return representation