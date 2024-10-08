from django.urls import path
from .views import CoursesAPIView,CourseAPIView, RatingsAPIView, RatingAPIView, RatingViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    # Abaixo: Buscando toda a coleção de cursos
    path('courses/',CoursesAPIView.as_view(), name='courses'),

    # Abaixo: Buscando um curso específico dentro de toda a coleção
    path('course/<int:pk>', CourseAPIView.as_view(), name='course'),

    # Buscando url de um curso específico
    path('course/<int:course_pk>/url', CoursesAPIView.as_view(),name='course_url'),

    # Abaixo: Buscando a coleção de AVALIAÇÕES em um curso específico #
    path('courses/<int:course_pk>/ratings', RatingsAPIView.as_view(), name='course_ratings'),

    # Abaixo: Buscando uma AVALIAÇÃO específica dentro de um curso específico #
    path('courses/<int:course_pk>/ratings/<int:rating_pk>', RatingAPIView.as_view(), name='course_rating'),

    # Abaixo: Buscando toda a coleção de avaliações criadas
    path('ratings/',RatingsAPIView.as_view(),name='ratings'),

    # Abaixo: Buscando uma avaliação específica de todas as avaliações criadas
    path('ratings/<int:pk>',RatingAPIView.as_view(),name='rating'),
    
]