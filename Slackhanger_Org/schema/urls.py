from django.urls import path, include
from rest_framework import routers
from . import views
from .api import SchemaViewSet

router = routers.DefaultRouter()
router.register('', SchemaViewSet, 'schema')


urlpatterns = [
    path('api/', include(router.urls)),
    path('extractData/<int:orgID>/<slug:dressType>', views.ExtractDataFromApi.as_view()),
]
