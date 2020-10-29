from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=250)
    revenue = models.FloatField()
    def __str__(self):
        return self.name
class Person(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.FloatField()
    company = models.ForeignKey('company', related_name='investor',on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


