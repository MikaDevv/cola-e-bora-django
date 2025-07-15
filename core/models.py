# core/models.py
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo_boras = models.IntegerField(default=100) 

    def __str__(self):
        return self.user.username

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    TIPO_CHOICES = [
        ('OFERTA', 'Ofereço Ajuda'),
        ('PEDIDO', 'Peço Ajuda'),
    ]
    ESTADO_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('CONCLUIDA', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    valor = models.IntegerField(help_text="Valor em Boras")
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo