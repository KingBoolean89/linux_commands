from rest_framework import routers
from .views import CommandViewSet

router = routers.DefaultRouter()
router.register('api/command', CommandViewSet, 'command')

urlpatterns = router.urls