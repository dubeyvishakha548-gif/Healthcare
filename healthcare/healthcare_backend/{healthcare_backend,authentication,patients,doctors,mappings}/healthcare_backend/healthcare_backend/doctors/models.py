from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctors'
    )
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Dr. {self.name} — {self.specialization}"
