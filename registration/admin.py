from django.contrib import admin
from django.db import models
from . models import SignUp, login
class SignUpModelAdmin(admin.ModelAdmin):
    list_display = ('name','username','sex','email','no','password')
    search_fields=('name','no')
    list_per_page=2

class loginModelAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    list_per_page=2
# Register your models here.
admin.site.register(SignUp, SignUpModelAdmin)
admin.site.register(login,loginModelAdmin)
