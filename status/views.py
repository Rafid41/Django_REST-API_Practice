# status\views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer

# Create your views here.


# MIXINS
# create model
class StatusListCreateAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # post request er jnno eta use hy, default post fn
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetail_Delete_UpdateView(
    generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin
):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # put request, mane update er jnno shob field lagbe
        return self.update(request, *args, **kwargs)
