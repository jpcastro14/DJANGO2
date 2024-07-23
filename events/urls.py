from django.urls import path
from .views import EventsAPIView,EventAPIView, TechCrewsAPIView,TechCrewAPIView, RolesAPIView,RoleAPIView, MaterialsAPIView,MaterialAPIView

urlpatterns = [

    path('events/', EventsAPIView.as_view(), name='events'),
    path('event/<int:pk>', EventAPIView.as_view(), name='event'),

    path('techs/', TechCrewsAPIView.as_view(), name='technicians'),
    path('tech/<int:pk>', TechCrewAPIView.as_view(), name='technician'),

    path('roles/', RolesAPIView.as_view(), name='roles'),
    path('role/<int:pk>', RoleAPIView.as_view(), name='role'),
    
    path('materials/', MaterialsAPIView.as_view(), name='materials'),
    path('material/<int:pk>', MaterialAPIView.as_view(), name='material')


]