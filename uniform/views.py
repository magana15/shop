from rest_framework.viewsets import ModelViewSet
from .models import Uniform
from .serializers import UniformSerializer


class UniformModelViewSet(ModelViewSet):
    queryset = Uniform.objects.all()
    serializer_class = UniformSerializer
