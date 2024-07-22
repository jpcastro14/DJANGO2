from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Roles, Material, Event, Techcrew
from .serializers import RolesSerializer, MaterialSerializer, EventSerializer, TechcrewSerializer


# Plural para tratar de listagens e inserção se coleções
class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MaterialsAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class RolesAPIView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

 
class TechCrewsAPIView(generics.ListCreateAPIView):
    queryset = Techcrew.objects.all()
    serializer_class = TechcrewSerializer
    test = 1


# Classes a serem aprendidas

#class EventAPIView():

#class MaterialAPIView():

#class RoleAPIView():    
    
#class TechCrewAPIView():

    
    


    



