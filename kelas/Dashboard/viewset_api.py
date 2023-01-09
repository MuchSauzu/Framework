from Dashboard.models import Jenis
from Dashboard.serializers import JenisSerializer
from rest_framework import viewsets

class JenisViewset(viewsets.ModelViewSet):
    queryset = Jenis.objects.all()
    serializer_class = JenisSerializer