from rest_framework import serializers
from djr.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','samplesheet','owner')
        read_only_fields = ('created', 'owner')