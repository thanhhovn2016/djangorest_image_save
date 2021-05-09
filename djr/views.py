from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from djr.models import Snippet
from djr.serializers import FileUploadSerializer


class FileUploadViewSet(ModelViewSet):
    
    queryset = Snippet.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('samplesheet'))