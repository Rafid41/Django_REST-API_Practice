# status\views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
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
# class StatusListView(APIView):
#     def get(self, request):
#         all_status = Status.objects.all()
#         serializer = StatusSerializer(all_status, many=True)
#         return Response(serializer.data)


# same class(above) er alternative
# generics.ListAPIView
class StatusListView(generics.ListAPIView):
    # default name
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# generics.createAPIViews  => only for creating new views
class StatusCreateView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# detailView
class StatusDetailView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # jodi pk diye search korte na chai, taile
    # lookup_field= e bole dte hbe ki diye search korte chai


# UpdateView
class StatusUpdateView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# deleteView
class StatusDeleteView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer