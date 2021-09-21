from django.db import models
# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    email = models.EmailField()
    no = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    