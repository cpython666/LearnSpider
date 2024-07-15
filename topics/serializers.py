from rest_framework import serializers
from .models import Topics

class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'
