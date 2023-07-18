from rest_framework import viewsets,generics, status
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializers, CursoSerializers, MatriculaSerializers, ListaMatriculasAlunoSerializers, ListaAlunosPorCursoSerializers, AlunoSerializersV2
from rest_framework.response import Response

class AlunosViewSet(viewsets.ModelViewSet):
    """"" Exibindo todos os alunos """""
    queryset = Aluno.objects.all()
    def get_serializer_class(self): # Consulta se a requisição foi feita para a versão dois ou um na url
        if self.request.version == 'v2':
            return AlunoSerializersV2
        else:
            return AlunoSerializers

class CursosViewSet(viewsets.ModelViewSet):
    """"" Exibindo todos os cursos """""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status = status.HTTP_201_CREATED)
            id = str(serializer.data ['id'])
            response ['Location'] = self.request.build_absolute_uri() + id
            return response


class MatriculaViewSet(viewsets.ModelViewSet):
    """"" Exibindo todas as matriculas """"" # http//aaaaaaaaaaaa/matricula
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializers
    http_method_names = ['get', 'post','put','path']

class ListaMatriculasAluno(generics.ListAPIView):
    """"" Listando todas as matriculas """"" # http//aaaaaaaaaaaa/aluno/2/matricula
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk']) # pegando o aluno especifico passado na requição 
        return queryset
    serializer_class = ListaMatriculasAlunoSerializers

class ListaAlunosPorCurso(generics.ListAPIView):
    """"" Listando todos os alunos matriculados em um curso """""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosPorCursoSerializers


    
