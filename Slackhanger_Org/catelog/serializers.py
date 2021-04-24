from rest_framework import serializers
from .models import Catelog

# Catelog Serializer
class CatelogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Catelog
    fields = '__all__'