from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = (
            'id', 'created_by', 'name', 'age', 'gender',
            'contact_number', 'address', 'medical_history',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')
