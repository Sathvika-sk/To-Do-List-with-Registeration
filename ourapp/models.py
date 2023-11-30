from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .manager import UserManager
# Create your models here.
class newuser( AbstractUser):
    username=None
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    email=models.EmailField(max_length=50,unique=True)
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    dob=models.DateField(null=False)
    gender=models.CharField(max_length=10,null=False)
    highestqualification=models.CharField(max_length=20,null=False)
    specialisation=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=400,null=False)
    password=models.CharField(max_length=50,null=False)
    objects = UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','gender','dob','address','specialisation','highestqualification','password']

