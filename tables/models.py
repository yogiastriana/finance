from django.db import models

class CompanyData(models.Model):
    symbol = models.CharField(max_length=10)
    shortname = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    marketcap = models.BigIntegerField()
    previous_close = models.FloatField()
    beta = models.FloatField()
    baw = models.FloatField()
    amin = models.FloatField()
    amax = models.FloatField()
    correlation = models.FloatField()
