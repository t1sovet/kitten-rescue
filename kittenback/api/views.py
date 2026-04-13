from rest_framework import viewsets, permissions, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .models import Kitten, Message, Address, AdoptionRequest
from .serializers import (
    KittenSerializer,
    MessageSerializer,
    AddressSerializer,
    UserSerializer,
    RegisterSerializer,
    AdoptionRequestSerializer
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


class AdoptionRequestViewSet(viewsets.ModelViewSet):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def get_queryset(self):
        return AdoptionRequest.objects.filter(
            Q(requester=self.request.user) | Q(kitten__owner=self.request.user)
        )

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        adoption_request = self.get_object()

        if adoption_request.kitten.owner != request.user:
            return Response(
                {"error": "Доступ запрещен"}, status=status.HTTP_403_FORBIDDEN
            )

        adoption_request.status = AdoptionRequest.Status.APPROVED
        adoption_request.save()

        kitten = adoption_request.kitten
        kitten.owner = adoption_request.requester
        kitten.is_adopted = True
        kitten.save()

        return Response({"status": "Заявка одобрена, владелец изменен"})

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        adoption_request = self.get_object()

        if adoption_request.kitten.owner != request.user:
            return Response({"error": "Вы не можете отклонить эту заявку"}, status=403)

        adoption_request.status = AdoptionRequest.Status.REJECTED
        adoption_request.save()

        return Response({"status": "Заявка отклонена"})


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
