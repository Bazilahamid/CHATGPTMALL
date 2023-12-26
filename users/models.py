from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class CustomUser(AbstractBaseUser):
    
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True)
    user_bio = models.TextField(max_length=100, null=True)
    user_profile_image = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD =['phone_number']
    REQUIRED_FIELDS =[]