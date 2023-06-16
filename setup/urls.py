from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet,CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosPorCurso
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matricula')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ), # quando for redenrizado alunos/ retorna def alunos
    path('aluno/<int:pk>/matriculas/',ListaMatriculasAluno.as_view()), # procurando matriculas de um aluno especifico 
    path('curso/<int:pk>/matriculas/', ListaAlunosPorCurso.as_view())
]
