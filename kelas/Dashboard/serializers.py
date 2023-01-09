from Dashboard.models import Jenis
from rest_framework import serializers

class JenisSerializer(serializers.ModelSerializer):
    class Meta:
       model = Jenis
       fields = ['id','nama','ket']