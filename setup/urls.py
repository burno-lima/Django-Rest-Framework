from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewsSet, basename='Alunos')
router.register('cursos', CursosViewsSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

