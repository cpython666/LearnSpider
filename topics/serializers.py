from rest_framework import serializers
from .models import Topics
from LearnSpider.settings import topics_path_prefix
class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        response_path = representation.get('response_path')
        if response_path:
            representation['response_path'] = f"{topics_path_prefix}{response_path}"
        return representation