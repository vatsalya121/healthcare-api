from django.urls import path
from .views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patients'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]
