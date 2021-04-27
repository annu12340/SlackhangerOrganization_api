from .models import Schema
from rest_framework import viewsets, permissions
from .serializers import SchemaSerializer


class SchemaViewSet(viewsets.ModelViewSet):
    #Use this or testing purpose : permission_classes = [permissions.AllowAny, ]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)