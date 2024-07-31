from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import  Course, Rating
from .serializers import CourseSerializer, RatingSerializer 
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # kwargs: Serve para a função receber diferentes tipos de argumentos (name="João", age=27)

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id = self.kwargs.get('course_pk'))
        return self.queryset.all()

class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
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




    

    
    


    



