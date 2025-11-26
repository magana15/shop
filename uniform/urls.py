from rest_framework.routers import DefaultRouter
from .views import UniformModelViewSet


router = DefaultRouter()

router.register(r"uniform",UniformModelViewSet)

urlpatterns = router.urls
