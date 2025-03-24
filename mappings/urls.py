from django.urls import path
from .views import MappingListCreateView, PatientDoctorListView, AssignDoctorView, MappingDeleteView, RemoveDoctorView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mappings'),
    path('<int:patient_id>/', PatientDoctorListView.as_view(), name='patient-mappings'),
    path('<int:pk>/delete/', MappingDeleteView.as_view(), name='mapping-delete'),
    path('api/mappings/', AssignDoctorView.as_view(), name='assign_doctor'),
    path('api/mappings/<int:patient_id>/', PatientDoctorListView.as_view(), name='patient_doctors'),
    path('api/mappings/delete/<int:id>/', RemoveDoctorView.as_view(), name='remove_doctor'),
]
