from rest_framework.viewsets import ModelViewSet
from livraria.models import Categoria, Editora, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, LivroDetailSerializer, LivroSerializer, LivroListSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer

class LivroListViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
