from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    crm = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.nome