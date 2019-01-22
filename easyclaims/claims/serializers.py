from django import forms
from .models import List
from rest_framework import serializers

class ListForm(serializers.ModelSerializer):
    class Meta:
        model=List
        fields=["name","dob","address","policyNo","claimNo","typeOfClaim","details"]

