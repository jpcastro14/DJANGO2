from django.urls import path
from .views import CourseAPIView, RatingAPIView

urlpatterns = [

    path('/courses',CourseAPIView.as_view(), name='Courses'),

    path('/ratings',RatingAPIView.as_view(),name='Ratings'),

]