from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from patients.models import Patient


class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve all patient-doctor mappings."""
        mappings = PatientDoctorMapping.objects.select_related('patient', 'doctor').all()
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Assign a doctor to a patient."""
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MappingByPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        """Get all doctors assigned to a specific patient."""
        patient = get_object_or_404(Patient, pk=patient_id)
        mappings = PatientDoctorMapping.objects.filter(patient=patient).select_related('doctor')
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove a doctor from a patient."""
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        mapping.delete()
        return Response(
            {'message': 'Doctor removed from patient successfully.'},
            status=status.HTTP_204_NO_CONTENT,
        )
