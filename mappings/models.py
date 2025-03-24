from django.db import models
from django.conf import settings
from doctors.models import Doctor
from patients.models import Patient

class DoctorPatientMapping(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.patient.name}"
