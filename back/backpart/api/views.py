from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from api.models import Address, Kitten, Message
from .serializers import KittenSerializer, AddressSerializer, MessageSerializer

# Create your views here.
class KittenListCreateView(generics.ListCreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer

    def get_permissions(self):
        # Allow anyone to view the list, but only logged-in users to post
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        # Automatically set the owner to the current user
        serializer.save(owner=self.request.user)

# Handles GET, PUT, and DELETE for a single kitten by ID
class KittenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



# @api_view(['GET', 'POST'])
# def MessageAPIView(request):
#     if request.method == 'GET':
#         messages = Message.objects.all()
#         return Response([{"id": msg.id, "content": msg.content, "sender": msg.sender.username} for msg in messages])
#     elif request.method == 'POST':
#         content = request.data.get('content')
#         if content:
#             message = Message.objects.create(content=content, sender=request.user)
#             return Response({"id": message.id, "content": message.content, "sender": message.sender.username}, status=201)
#         return Response({"error": "Content is required"}, status=400)
    
# class AdoptionRequestView(APIView):
#     def get(self, request):
#         adoption_requests = AdoptionRequest.objects.all()
#         return Response([{"id": req.id, "kitten": req.kitten.id, "request_for": req.request_for.username, "request_from": req.request_from.username} for req in adoption_requests])
    
#     def post(self, request):
#         serializer = AdoptionRequestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)