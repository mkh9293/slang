from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Member(models.Model):
    m_id = models.CharFiled.unique(max_length=10)
    m_email = models.EmailFiled.unique
    m_pass = models.CharFiled
    
    def __str__(self):
        return self.m_id
    
class Team(models.Model):
    t_name = models.CharFiled.unique(max_length=20)
    
    def __str__(self):
        return self.t_name