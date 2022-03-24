from django.db import models

class User(models.Model):

    email = models.EmailField('email', max_length=50)
    pwd = models.CharField('password', max_length=50)

    def __str__(self):
        return self.title
