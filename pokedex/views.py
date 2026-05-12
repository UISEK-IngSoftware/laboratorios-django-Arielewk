from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import get_object_or_404, redirect, render
from pokedex.forms import PokemomForm



def index(request):
    pokemons = Pokemon.objects.all() #select * from pokedex_pokemon
    trainers = Trainer.objects.all() 
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
        }, 
        request))

def pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request)) 


def trainer_details(request, id:int):
    trainer = Trainer.objects.get(id=id) #select * from pokedex_pokemon where id = id
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request)) 

def add_pokemon(request):
    if request.method == "POST":
        form = PokemomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemomForm()

    return render(request, 'pokemon_form.html', {'form': form})


def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemomForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemomForm(instance=pokemon)

    return render(request, 'pokemon_form.html', {'form': form})
    
def delete_pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    pokemon.delete()
    return redirect('pokedex:index')