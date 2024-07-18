from django.urls import path
from .views import EventsAPIView, TechCrewsAPIView, RolesAPIView, MaterialsAPIView

urlpatterns = [
    path('event/', EventsAPIView.as_view(), name='events'),
    path('techs/', TechCrewsAPIView.as_view(), name='technician'),
    path('roles/', RolesAPIView.as_view(), name='roles'),
    path('materials/', MaterialsAPIView.as_view(), name='materials')


]