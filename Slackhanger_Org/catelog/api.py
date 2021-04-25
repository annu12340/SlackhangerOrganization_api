from .models import Catelog
from rest_framework import viewsets, permissions
from .serializers import CatelogSerializer


class CatelogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = CatelogSerializer

    def get_queryset(self):
        return self.request.user.catelog.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)