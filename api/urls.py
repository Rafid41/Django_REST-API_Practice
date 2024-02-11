# api\urls.py
from django.urls import path
from status.views import StatusViewer, StatusListView

urlpatterns = [
    path('status/<int:id>/', StatusViewer.as_view(), name='status_view'),
    path('statuses/', StatusListView.as_view()),
]
