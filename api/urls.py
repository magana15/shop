from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CustomerModelViewSet


router = DefaultRouter()
router.register(r'customer', CustomerModelViewSet)

urlpatterns = router.urls

"""[
    

    path("", views.home),
    path("about/", views.about),
    path("customer/", CustomerListAPIView.as_view),

]"""
