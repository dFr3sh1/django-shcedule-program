from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Useer class with an argument AbstractUseer

    Args:
        AbstractUser User type to assign rols for users
    """
    COACH = 'COACH'
    CUSTOMER = 'CUSTOMER'
    STAFF = 'STAFF'
    
    
    ROLE_CHOICES = (
        (COACH, 'Coach'),
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff')        
        )
    
    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle') 
    
