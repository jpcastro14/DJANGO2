from django.contrib import admin

# Register your models here.

from .models import Course, Rating

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','url']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['course','name','email','comment','rating']


