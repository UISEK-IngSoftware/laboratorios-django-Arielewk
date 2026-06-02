from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import get_object_or_404, redirect, render
from pokedex.forms import PokemomForm, TrainerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required



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

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemomForm()

    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()

    return render(request, 'pokemon_form.html', {'form': form})

@login_required
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

@login_required
def delete_pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id) #select * from pokedex_pokemon where id = id
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_trainer(request, id:int):
    trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'
