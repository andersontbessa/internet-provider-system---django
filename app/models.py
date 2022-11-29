from django.db import models

class Animals(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    birthDate = models.CharField(max_length=50, null=False, blank=False)
    cpf = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(max_length=30, null=False, blank=False)
    updateOn = models.DateTimeField(auto_now_add = True)
