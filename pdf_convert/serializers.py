from rest_framework import serializers
from .models import ConvertedUrls

class Html_to_PDFSerializer(serializers.Serializer):
    url = serializers.URLField()

    def create(self, validated_data):
        return ConvertedUrls.objects.create(**validated_data)