from django.contrib import admin

# Register your models here.

from .models import Roles, Techcrew, Material, Event

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['Rname']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['Mrole','Mname']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['Evname','Evdate','Evleader','Evlocation','Evmaterial']

@admin.register(Techcrew)
class TechcrewAdmin(admin.ModelAdmin):
    list_display = ['Tname','Trole']