from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Roles, Material, Event, Techcrew
from .serializers import RolesSerializer, MaterialSerializer, EventSerializer, TechcrewSerializer


class EventAPIView(APIView):
    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many = True)
        return Response(serializer.data)

class MaterialAPIView(APIView):
    def get(self,request):
        material = Material.objects.all()
        serializer = MaterialSerializer(material, many =True)
        return Response(serializer.data)
    
class RolesAPIView(APIView):
    def get (self,request):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many = True)
        return Response(serializer.data)
    
class TechCrewAPIView(APIView):
    def get (self, request):
        techcrew = Techcrew.objects.all()
        serializer = TechcrewSerializer(techcrew, many= True)
        return Response(serializer.data)
    


    



