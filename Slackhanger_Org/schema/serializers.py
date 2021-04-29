from rest_framework import serializers
from .models import Schema

# Schema Serializer
class SchemaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schema
    fields = '__all__'
