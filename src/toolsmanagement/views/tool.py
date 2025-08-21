# apps/api/views.py
from rest_framework import viewsets

from ..models import Tool
from ..serializers import ToolSerializer


class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

