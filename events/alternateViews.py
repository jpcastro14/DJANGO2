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
    
    def post(self,request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    

class MaterialAPIView(APIView):

    def get(self,request):
        material = Material.objects.all()
        serializer = MaterialSerializer(material, many =True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MaterialSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RolesAPIView(APIView):
    def get (self,request):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many = True)
        return Response(serializer.data)
    
    def post (self, request):
        serializer = RolesSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class TechCrewAPIView(APIView):
    def get (self, request):
        techcrew = Techcrew.objects.all()
        serializer = TechcrewSerializer(techcrew, many= True)
        return Response(serializer.data)
    
    def post (self, request):
        serializer = TechcrewSerializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    
    


    



