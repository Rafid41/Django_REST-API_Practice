# status\views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins, parsers, viewsets
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer

# Create your views here.


# ModelViewSet typically mixin k use kore
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
