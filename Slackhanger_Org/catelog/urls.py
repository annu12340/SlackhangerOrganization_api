from rest_framework import routers
from .api import CatelogViewSet

router = routers.DefaultRouter()
router.register('api/catelog', CatelogViewSet, 'catelog')

urlpatterns = router.urls