from rest_framework import viewsets, permissions, status
from .models import Schema
from .serializers import SchemaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import json

class SchemaViewSet(viewsets.ModelViewSet):
    #testing purpose -> permission_classes = [permissions.AllowAny, ]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user)

    #Todo: CHeck the data type of the incoming API schema
    #eg in our db {"color":char}, check if incoming API has color as a character
    @action(detail=False, methods=['post'])
    def extractDatafromAPI(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # json_data contains the API schema data that we give from the browser
            json_data = request.data

            # snippets contains the schema format from the db
            snippets=Schema.objects.filter(organization=json_data['organization']).filter(dress_type=json_data['dress_type']).values('schema_format')
            dic=snippets[0]["schema_format"]

            extracted_data={}
            for key, value in dic.items():
                print(key, 'is',json_data["schema_format"].get(key))
                extracted_data[key] = json_data["schema_format"].get(key)
            return Response({'message': json.dumps(extracted_data)})

        return Response({'status': status.HTTP_400_BAD_REQUEST,'message': 'Data is not valid, try again','error': serializer.errors})
