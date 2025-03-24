from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import DoctorPatientMapping,PatientDoctorMapping
from .serializers import DoctorPatientMappingSerializer, PatientDoctorMappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = DoctorPatientMapping.objects.all()
    serializer_class = DoctorPatientMappingSerializer
    permission_classes = [IsAuthenticated]
    
class PatientDoctorListView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

class MappingDeleteView(generics.DestroyAPIView):
    queryset = DoctorPatientMapping.objects.all()
    serializer_class = DoctorPatientMappingSerializer
    permission_classes = [IsAuthenticated]


class AssignDoctorView(generics.CreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        patient_id = request.data.get("patient")
        doctor_id = request.data.get("doctor")

        # Check if patient and doctor exist
        if not Patient.objects.filter(id=patient_id).exists():
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

        if not Doctor.objects.filter(id=doctor_id).exists():
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create Mapping
        mapping = PatientDoctorMapping.objects.create(patient_id=patient_id, doctor_id=doctor_id)
        return Response({"message": "Doctor assigned successfully"}, status=status.HTTP_201_CREATED)