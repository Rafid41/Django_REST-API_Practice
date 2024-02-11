# status\views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer

# Create your views here.


class StatusViewer(APIView):
    # jodi kew get request dey
    def get(self, request, **kwargs):
        id = kwargs.get('id')
        status = Status.objects.get(pk=id)
        serializer = StatusSerializer(status, many=False)
        return Response(serializer.data)



# all status
class StatusListView(APIView):
    def get(self, request):
        all_status = Status.objects.all()
        serializer = StatusSerializer(all_status, many=True)
        return Response(serializer.data)
