from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Schema
from .serializers import SchemaSerializer


class ExtractDataFromApi(APIView):
    def get(self, request, orgID, dressType):
        snippets = Schema.objects.filter(organization=orgID).filter(dress_type=dressType)
        serializer = SchemaSerializer(snippets,many=True)

        # schema_json contains the entire json data
        schema_json = serializer.data[0]
        schema_format = schema_json.get('schema_format')
        return Response(schema_format)

