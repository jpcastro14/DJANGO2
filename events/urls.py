from django.urls import path
from .views import EventAPIView, TechCrewAPIView, RolesAPIView, MaterialAPIView

urlpatterns = [
    path('events/', EventAPIView.as_view(), name='events'),
    path('techs/', TechCrewAPIView.as_view(), name='technician'),
    path('roles/', RolesAPIView.as_view(), name='roles'),
    path('materials/', MaterialAPIView.as_view(), name='materials')


]