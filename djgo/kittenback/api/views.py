from rest_framework import viewsets, permissions, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Kitten, Message, Address
from .serializers import (
    KittenSerializer,
    MessageSerializer,
    AddressSerializer,
    UserSerializer,
    RegisterSerializer
)


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer

    def get_queryset(self):
        queryset = Kitten.objects.all()
        owner_id = self.request.query_params.get("owner")
        available = self.request.query_params.get("available")

        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if available == "true":
            queryset = queryset.filter(owner__isnull=True)
        return queryset


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        queryset = Message.objects.all()
        tag = self.request.query_params.get("tag")
        if tag:
            queryset = queryset.filter(tag=tag)
        return queryset


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
