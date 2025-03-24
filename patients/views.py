from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only the patient profile associated with the logged-in user."""
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Prevent a user from creating multiple patient profiles."""
        if Patient.objects.filter(user=self.request.user).exists():
            return Response(
                {"error": "A patient profile already exists for this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=self.request.user)
        
        
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    def delete(self, request, *args, **kwargs):
        try:
            patient = self.get_object()
            patient.delete()
            return Response({"message": "Patient deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response({"error": "No Patient matches the given query."}, status=status.HTTP_404_NOT_FOUND)
    
    
class PatientUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if Patient.objects.filter(user=self.request.user).exists():
            return Response({"error": "A patient with this user already exists."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
