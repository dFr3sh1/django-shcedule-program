from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)    
    #email= models.EmailField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=1000, null=True)
    
    # def __str__(self) -> str:
    #     return f'{self.username ({self.start_time} -  {self.end_time})}'
    
    # def save(self, *args, **kwargs):
    #     #Ensure start  time  is aligned to 1O minuts intervals    
    #     minute = self.start_time.minute
    #     self.start_time -= timezone.timedelta(minutes=minute %10)
    #     #Set end time to 45 minutes after startime
    #     self.end_time = self.start_time + timezone.timedelt(minutes=45)
    #     super().save(*args, **kwargs)
        
    # class Meta:
    #     ordering = ["start_time"]
    
    
    
class User(AbstractUser):
    """
    User class with an argument AbstractUseer

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
    
