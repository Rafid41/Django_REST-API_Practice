# status\serializers.py
from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        # kon model and kon kon field serialize korbo
        model = Status
        fields = ['id', 'text', 'created_at', 'user']