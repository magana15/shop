from rest_framework import serializers
from .models import Uniform


class UniformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uniform
        fields = '__all__'
