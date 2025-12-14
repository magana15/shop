from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'customer', views.CustomerModelViewSet)

#urlpatterns += router.urls
urlpatterns = [
    

    path("", views.home),
    path("about/", views.about),
    path("customers/", views. CustomerModelViewSet.as_view),

]
urlpatterns += router.urls
