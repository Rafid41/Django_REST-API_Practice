# api\urls.py
from django.urls import path
from status.views import StatusListCreateAPIView, StatusDetail_Delete_UpdateView

urlpatterns = [
    path("status/", StatusListCreateAPIView.as_view(), name="status_view"),
    path("status/<pk>/", StatusDetail_Delete_UpdateView.as_view()),
]
