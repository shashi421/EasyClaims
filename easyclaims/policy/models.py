from django.db import models
class Policy(models.Model):

    policy_name=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    life_assureddetails=models.CharField(max_length=50)
    payment_information=models.IntegerField()
    premium_details=models.IntegerField()
# Create your models here.
