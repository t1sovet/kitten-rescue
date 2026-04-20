from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Kitten, Message

class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = ['id', 'name', 'description', 'owner', 'address', 'image']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'city', 'street', 'building_number']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'content', 'sender']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
    


# class MessageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content = serializers.CharField(max_length=255)
#     sender = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return Message.objects.create(**validated_data)

# class AdoptionRequestSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     kitten = serializers.PrimaryKeyRelatedField(queryset=Kitten.objects.all())
#     request_for = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     request_from = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     def create(self, validated_data):
#         return AdoptionRequest.objects.create(**validated_data)