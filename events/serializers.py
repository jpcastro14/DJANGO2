from rest_framework import serializers
from .models import Course, Rating


class RatingSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField()

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
                  ]
        
#class LowRatingSerializer(serializers.ModelSerializer):

class CourseSerializer(serializers.ModelSerializer):

    # 1. Nested Relationship - Boa solução para a WL Audio pois ja retorna todos os materiais cadastrados para cada evento
    ratings = RatingSerializer(many=True, read_only=True);

    # 2. HyperLinked Related Field - Gera um link em URI para o registro da avaliação específica
    #ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

    # 3. Primary Key Related Field - Retorna a chave primaria da 
    #ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 4. Slug Related Fields
    #ratings = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'creation',
            'active',
            'ratings'
        ]
