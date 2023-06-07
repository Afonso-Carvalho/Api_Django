# Converte os models como por exemplo class Aluno pra json e joga no banco de dados
from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # escolhe todos os argumentos