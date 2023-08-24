from django.db import models

class Cliente(models.Model):
    class Sexo(models.TextChoices):
        Feminino = "F", ("Feminino")
        Masculino = "M", ("Masculino")

    class Ativo(models.IntegerChoices):
        Nao = 0, ("Não")
        Sim = 1, ("Sim")

    nome = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=100, null=True)
    sexo = models.CharField(max_length=1, choices=Sexo.choices, null=True)
    ativo = models.IntegerField(choices=Ativo.choices, null=True)
    endereco = models.ManyToManyField("Endereco")

    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    cep = models.CharField(max_length=9, null=True)
    estado = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=100, null=True)
    logradouro = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.cep
    
