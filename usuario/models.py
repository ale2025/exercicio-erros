from django.db import models

# Create your models here.

class Pessoa(models.Model):
  GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('NB', 'Não-binário'),
    ('O', 'Outros'),
  )
  nome = models.CharField(max_length=255,)
  cpf = models.CharField(max_length=255, )
  email = models.EmailField(max_length=255,)
  telefone = models.IntegerField()
  genero = models.CharField(max_length=255,  choices=GENEROS  )
  ativo = models.BooleanField(default=True)

  def __str__(self):
    return self.nome

  