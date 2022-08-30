from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register('api/category', CategoryViewSet, 'category')

urlpatterns = router.urls