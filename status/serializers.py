# status\serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from status.models import Status


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)  # ekta user

    class Meta:
        # kon model and kon kon field serialize korbo
        model = Status
        fields = ['id', 'text', 'created_at', 'user']
