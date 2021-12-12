from django.db import models


# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    lote = models.CharField(max_length=100)

    def __str__(self):
        return self.lote

    endereco = models.CharField(max_length=255)
    areaconstruida = models.CharField(max_length=100)
    situacao = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')