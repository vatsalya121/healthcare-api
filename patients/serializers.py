from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate(self, data):
        """Ensure a user does not already have a patient profile."""
        user = self.context['request'].user
        if Patient.objects.filter(user=user).exists():
            raise serializers.ValidationError("A patient profile already exists for this user.")
        return data