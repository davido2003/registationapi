from django.db import models
from rest_framework import serializers, fields
from . models import SignUp, login

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ['name','username','sex','email','no','password']

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ['username','password']
        
