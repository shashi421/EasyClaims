from django import forms
from claims.models import List
from rest_framework import serializers

class ListForm(serializers.ModelSerializer):
    class Meta:
        model=List
        fields='__all__'

