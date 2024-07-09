from rest_framework import serializers
from .models import Roles,Material, Event, Techcrew


class TechcrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techcrew
        fields = [
            'id',
            'Tname',
            'Trole'
        ]

class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = [
            'id',
            'Rname'
        ]

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = [
            'id',
            'Mrole',
            'Mname'
        ]

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'Evname',
            'Evdate',
            'Evleader',
            'Evlocation',
            'Evmaterial'
        ]