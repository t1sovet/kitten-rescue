from rest_framework import serializers
from .models import Kitten

class KittenSerializeer(serializers.Serializer):
    class Meta:
        model = Kitten
        fiels = '__all__'