from django.db import models

# Create your models here.
class ConfirmarPresença(models.Model):
    nome = models.CharField(max_length=100)
    data_confirmacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"


class PresenteEscolhido(models.Model):
    nome_convidado = models.CharField(max_length=100)
    presente = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_convidado} - {self.presente}"