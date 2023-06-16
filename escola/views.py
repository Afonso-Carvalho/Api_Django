from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializers, CursoSerializers, MatriculaSerializers

class AlunosViewSet(viewsets.ModelViewSet):
    """"" Exibindo todos os alunos """""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializers

class CursosViewSet(viewsets.ModelViewSet):
    """"" Exibindo todos os cursos """""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

class MatriculaViewSet(viewsets.ModelViewSet):
    """"" Exibindo todas as matriculas """""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializers