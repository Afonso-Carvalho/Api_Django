# Converte os models como por exemplo class Aluno pra json e joga no banco de dados
from rest_framework import serializers
from escola.models import Aluno, Curso , Matricula

class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # escolhe todos os argumentos

class MatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Matricula
        exclude = [] # mesma coisa que fields = '__all__' so q o campo q eu passar no [] não ira aparecer