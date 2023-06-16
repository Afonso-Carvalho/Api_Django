from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento') # exibir campus no admin
    list_display_links = ('id', 'nome') # caso queira mudar algo em um aluno sera clicado em um desses link
    search_fields = ('nome',) #busca
    list_per_page = 20 #lista paginas

admin.site.register(Aluno,Alunos) #registra no /admin

class Cursos (admin.ModelAdmin):
    list_display = ('id','codigo_curso', 'descricao' ) # exibir campus no admin
    list_display_links = ('id', 'codigo_curso') # caso queira mudar algo em um aluno sera clicado em um desses link
    search_fields = ('codigo_curso',) #busca
    list_filter = ("nivel",)

admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula,Matriculas)