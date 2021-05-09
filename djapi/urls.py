from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from djr.models import Snippet
from djr.serializers import FileUploadSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# Serializers define the API representation.
class FileUploadViewSet(viewsets.ModelViewSet):
    
    queryset = Snippet.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       samplesheet=self.request.data.get('samplesheet'))


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'test', FileUploadViewSet)

    


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
	settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
