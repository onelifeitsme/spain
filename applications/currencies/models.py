from django.db import models

"""
Модуль на будущее развитие
"""

class Currency(models.Model):
    name = models.CharField('Currency', max_length=3, help_text="Currency Code (ISO 4217)")
    symbol = models.CharField(max_length=1, help_text="Currency sign, to be used when printing amounts.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'