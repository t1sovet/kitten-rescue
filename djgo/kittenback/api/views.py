from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def kitten_list(request):
    kittens = Kitten.objects.all()
    return Response(KittenSerializeer(kittens).data)