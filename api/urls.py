# api\urls.py
from django.urls import path
from rest_framework import routers

from status.views import StatusViewSet

router = routers.SimpleRouter()
# register viewsets from views and url pattern
# multiple register kora jabe
router.register(r"status", StatusViewSet)


urlpatterns = [] + router.urls
