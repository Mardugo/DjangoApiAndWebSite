from django.db import models

class User(models.Model):
    givenName = models.CharField(max_length=100)
    firstFamilyName = models.CharField(max_length=100)
    secondFamilyName = models.CharField(max_length=100)
    age = models.IntegerField()
    accountName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name