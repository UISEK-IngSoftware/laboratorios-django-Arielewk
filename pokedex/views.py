from django.http import HttpResponse
from django.template import loader
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all() #select * from pokedex_pokemon
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request)) 