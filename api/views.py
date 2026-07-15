from rest_framework import permissions
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializers import ( PokemonSerializer,TrainerSerializer,)


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('id')
    serializer_class = PokemonSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [
                permissions.AllowAny,
            ]
        else:
            permission_classes = [
                permissions.IsAuthenticated,
            ]

        return [
            permission()
            for permission in permission_classes
        ]


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('id')
    serializer_class = TrainerSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

