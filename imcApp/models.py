from django.db import models


class Profile(models.Model):
    peso = models.FloatField()
    altura = models.FloatField()


    def calcular_imc(self):
        if self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        return None



