from rest_framework import viewsets, permissions
from .models import Schema
from .serializers import SchemaSerializer

class SchemaViewSet(viewsets.ModelViewSet):
    #Use this or testing purpose : permission_classes = [permissions.AllowAny, ]
    permission_classes = [permissions.AllowAny,]
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user)