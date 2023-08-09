from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet,CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosPorCurso
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ), # quando for redenrizado alunos/ retorna def alunos
    path('alunos/<int:pk>/matriculas/',ListaMatriculasAluno.as_view()), # procurando matriculas de um aluno especifico 
    path('cursos/<int:pk>/matriculas/', ListaAlunosPorCurso.as_view())
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


