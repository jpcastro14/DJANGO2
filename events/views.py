from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import  Course, Rating
from .serializers import CourseSerializer, RatingSerializer 


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer 


""" # Plural para tratar de GET e POST
class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Singular para os demais verbos HTTP
class EventAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# -------------------------------------------------

class MaterialsAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

# --------------------------------------------------

class RolesAPIView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class RoleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

# ------------------------------------------------    
 
class TechCrewsAPIView(generics.ListCreateAPIView):
    queryset = Techcrew.objects.all()
    serializer_class = TechcrewSerializer

class TechCrewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Techcrew.objects.all()
    serializer_class = TechcrewSerializer
 """




    

    
    


    



