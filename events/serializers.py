from rest_framework import serializers
from .models import Course, Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = { 'email':{'write_only':True}}

        model = Rating
        fields = [
                  'id',
                  'course',
                  'name',
                  'email',
                  'comment',
                  'rating',
                  'created',
                  'updated',]

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'criacao',
            'active'
        ]