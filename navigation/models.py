from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    Username = models.TextField(null=False)
    Password = models.TextField(null=False)
    ticket = models.TextField(null=False)
    Mark = models.TextField(null=False)
    Power = models.TextField(null=False)


class Data(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    urlname = models.TextField(null=False)
    url = models.TextField(null=False)