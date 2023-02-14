from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, default="")
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    obs = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao
