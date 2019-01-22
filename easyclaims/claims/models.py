from django.db import models                                                                                                                        
import uuid
import random
  
 # Create your models her
CLAIM_CHOICES = (
     ('car','Car Claim'),
     ('home', 'Home Claim'),
     ('health','Health Claim'),
    )
 
 # Create your models here.
class List(models.Model):
      name=models.CharField(max_length=100)
      dob = models.DateField()
      address = models.CharField(max_length=500)
      policyNo=models.CharField(max_length=8)
      claimNo =random.choice(range(1,8))
      typeOfClaim=models.CharField(max_length=6, choices=CLAIM_CHOICES, default='')
      details=models.CharField(max_length=500)
      status=models.CharField(max_length=500)

