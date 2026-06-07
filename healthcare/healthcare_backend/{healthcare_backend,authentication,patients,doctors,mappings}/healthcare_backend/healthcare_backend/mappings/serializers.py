from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class MappingSerializer(serializers.ModelSerializer):
    patient_detail = PatientSerializer(source='patient', read_only=True)
    doctor_detail = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = (
            'id', 'patient', 'doctor', 'notes',
            'assigned_at', 'patient_detail', 'doctor_detail',
        )
        read_only_fields = ('id', 'assigned_at', 'patient_detail', 'doctor_detail')

    def validate(self, data):
        if PatientDoctorMapping.objects.filter(
            patient=data['patient'], doctor=data['doctor']
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )
        return data
