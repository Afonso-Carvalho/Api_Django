from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status

class AlunoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome = 'Test-test-1',
            rg = '523339697',
            cpf = '30870793080',
            data_nascimento = '2001-12-15',
            foto = '',
        )

    def test_requisicao_get_para_listar_alunos(self):
        """Teste para verificar se a requisição GET para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_requisicao_post_em_alunos(self):
        data = {
            'nome' : 'Test-test-2',
            'rg' : '523339657',
            'cpf' : '30870793080',
            'data_nascimento' : '2001-10-15',
            'foto' : '',
        }
        response = self.client.post(self.list_url,data=data)
        self.assertEquals(response.status_code,status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_alunos(self):
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_um_aluno(self):
        data = {
            'nome' : 'Test-test-1',
            'rg' : '523349697',
            'cpf' : '30870793080',
            'data_nascimento' : '2001-12-15',
            'foto' : '',
        }
        response = self.client.put('/alunos/1/',data=data)
        self.assertEquals(response.status_code,status.HTTP_200_OK)