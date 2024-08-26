from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[ #essa regra e pra só deixar entrar o que eu quiser nesse campo
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas'), #primeiro valor é o minimo possivel e o segundo valor é msg de erro q retorna ao tentar passar a regra.
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas')
        ]
    )
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return str(self.movie)