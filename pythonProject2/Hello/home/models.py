from django.db import models

# Create your models here.
'''
makemigration --> create and save in a file
migrate --> apply the pending changes created by makemigrations'''

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone =  models.CharField(max_length=12)
    email =  models.CharField(max_length=122)
    desc = models.TextField()


    def  __str__(self):
        return self.name+self.email




