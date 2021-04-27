from rest_framework import routers
from .api import SchemaViewSet

router = routers.DefaultRouter()
router.register('api', SchemaViewSet, 'schema')

urlpatterns = router.urls