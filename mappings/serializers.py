from rest_framework import serializers
from .models import DoctorPatientMapping

class DoctorPatientMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorPatientMapping
        fields = '__all__'
