from rest_framework.test import APITestCase
from escola.models import Curso,Aluno,Matricula
from django.urls import reverse
from rest_framework import status

class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Matriculas-list')
        self.curso= Curso.objects.create(codigo_curso = 'CTT1', descricao = 'Curso teste 1', nivel = 'B')
        self.aluno = Aluno.objects.create(
            nome="Fulano",
            rg="123456789", 
            cpf="12345678901", 
            data_nascimento="1990-01-01", 
            celular="999999999"
        )
        self.matricula = Matricula.objects.create(curso=self.curso, aluno=self.aluno,periodo = 'M')
    
    
    def test_get_matricula(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_post_matricula(self):
        data = {
            'periodo':'V',
            'aluno' : self.aluno.pk, # usando a primary key de aluno
            'curso' : self.curso.pk, # usando a primary key de curso
        }
        response = self.client.post(self.list_url,data=data)
        self.assertEquals(response.status_code,status.HTTP_201_CREATED)

    def test_delete_matricula(self):
        response = self.client.delete('/matriculas/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_matriculas(self):
        data = {
            'periodo': 'N',
            'aluno' : self.aluno.pk, # usando a primary key de aluno
            'curso' : self.curso.pk, # usando a primary key de curso
        }
        response = self.client.put('/matriculas/1/',data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)