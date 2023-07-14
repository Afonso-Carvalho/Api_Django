from rest_framework import viewsets,generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializers, CursoSerializers, MatriculaSerializers, ListaMatriculasAlunoSerializers, ListaAlunosPorCursoSerializers, AlunoSerializersV2
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseViewSet:
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AlunosViewSet(BaseViewSet,viewsets.ModelViewSet):
    """"" Exibindo todos os alunos """""
    queryset = Aluno.objects.all()
    def get_serializer_class(self): # Consulta se a requisição foi feita para a versão dois ou um na url
        if self.request.version == 'v2':
            return AlunoSerializersV2
        else:
            return AlunoSerializers


class CursosViewSet(BaseViewSet,viewsets.ModelViewSet):
    """"" Exibindo todos os cursos """""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

class MatriculaViewSet(BaseViewSet,viewsets.ModelViewSet):
    """"" Exibindo todas as matriculas """"" # http//aaaaaaaaaaaa/matricula
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializers

class ListaMatriculasAluno(BaseViewSet,generics.ListAPIView):
    """"" Listando todas as matriculas """"" # http//aaaaaaaaaaaa/aluno/2/matricula
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk']) # pegando o aluno especifico passado na requição 
        return queryset
    serializer_class = ListaMatriculasAlunoSerializers

class ListaAlunosPorCurso(BaseViewSet, generics.ListAPIView):
    """"" Listando todos os alunos matriculados em um curso """""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosPorCursoSerializers


    
