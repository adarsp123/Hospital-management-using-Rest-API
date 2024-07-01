from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, PatientRecordViewSet, DepartmentViewSet, LoginAPI, RegisterAPI, LogoutAPI

urlpatterns = [
    # URL patterns for viewsets
    path('doctors/', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='doctor-detail'),

    path('patients/', PatientViewSet.as_view({'get': 'list', 'post': 'create'}), name='patient-list-create'),
    path('patients/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patient-detail'),

    path('patient_records/', PatientRecordViewSet.as_view({'get': 'list', 'post': 'create'}), name='patientrecord-list-create'),
    path('patient_records/<int:pk>/', PatientRecordViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patientrecord-detail'),

    path('departments/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='department-detail'),

]