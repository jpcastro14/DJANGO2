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

# ----------------------------- API V1 ----------------------------- #

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id = self.kwargs.get('course_pk'))
        return self.queryset.all()


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

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(), course_id=self.kwargs.get('course_pk'), pk=self.kwargs.get('rating_pk'))
        return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('rating_pk'))


# ----------------------------- API V2 ----------------------------- #

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def Ratings(self, request, pk=None):
        course = self.get_object()
        serializer = RatingSerializer(course.ratings.all(), many=True)
        return Response(serializer.data)

''' VIEWSET PADRÃO 
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
''' 

# VIEWSET CUSTOMIZADA ---------------------------------------------- #

class RatingViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    viewsets.GenericViewSet):
    
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    


    



