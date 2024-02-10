# api\urls.py
from django.urls import path
from status.views import StatusViewer

urlpatterns = [
    path('status/<id:str>/', StatusViewer.as_view(), name='status_view'),
]
