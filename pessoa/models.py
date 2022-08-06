from turtle import mode
from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)# quando quiser que aceite obrigatorio  ou vazio -  null=True, blank=True
    data_nascimento = models.DateTimeField(null=True)# não é obrigatório
    ativa = models.BooleanField(default=True)# padrao ativo
    
    
