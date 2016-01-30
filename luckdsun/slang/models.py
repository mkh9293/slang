from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Member(models.Model):
<<<<<<< HEAD
    m_id = models.CharField(max_length=10, unique=True)
    m_mail = models.EmailField
    m_pass = models.CharField(max_length=10)
=======
    m_id = models.CharField(max_length=10,unique=True)
    m_email = models.CharField(max_length=30,unique=True)
    m_pass = models.CharField(max_length=60)
>>>>>>> a52aa22a16dbb75a97c49c2c86d2c5ecb3ac5ad9
    
    def __str__(self):
        return self.m_id
    
class Team(models.Model):
    t_name = models.CharField(max_length=20,unique=True)
    m_idx = models.ManyToManyField(Member)
    
    def __str__(self):
        return self.t_name