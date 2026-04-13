from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Kitten, Message, AdoptionRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "city", "street", "building_number"]


class KittenSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source="owner.username")

    address_detail = AddressSerializer(source="address", read_only=True)

    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = Kitten
        fields = [
            "id",
            "name",
            "breed",
            "age_months",
            "description",
            "image",
            "owner",
            "owner_name",
            "is_adopted",
            "address",
            "address_detail",
        ]
        read_only_fields = ["is_adopted"]


class AdoptionRequestSerializer(serializers.ModelSerializer):
    requester_name = serializers.ReadOnlyField(source="requester.username")
    kitten_name = serializers.ReadOnlyField(source="kitten.name")

    class Meta:
        model = AdoptionRequest
        fields = [
            "id",
            "kitten",
            "kitten_name",
            "requester",
            "requester_name",
            "message",
            "status",
            "created_at",
        ]
        read_only_fields = ["requester", "status"]


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.ReadOnlyField(source="sender.username")
    tag_display = serializers.CharField(source="get_tag_display", read_only=True)

    class Meta:
        model = Message
        fields = [
            "id",
            "sender",
            "sender_name",
            "content",
            "timestamp",
            "tag",
            "tag_display",
            "kitten",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user
