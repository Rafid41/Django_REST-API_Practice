# status\views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins, parsers
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer

# Create your views here.


# eita typically mixin k use kore
class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


# eita typically mixin k use kore
class StatusDetail_Delete_UpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
