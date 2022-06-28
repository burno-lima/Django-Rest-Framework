from rest_framework import viewsets
from escola.models import Aluno, Cursos
from escola.serializer import AlunoSerializer, CursoSerializer


class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer
