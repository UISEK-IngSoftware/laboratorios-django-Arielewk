from django.db import models


class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pokemon(models.Model):
    name = models.CharField(max_length=100)

    POKEMON_TYPES = [
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
    ]

    type = models.CharField(max_length=1, choices=POKEMON_TYPES, null=False)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null= True)
    picture = models.ImageField(upload_to="pokemon_images", null=True, blank=True)

 

    def __str__(self):
        return self.name