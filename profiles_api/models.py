from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#from django.utils.timezone import datetime
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self, email, name,height,weight,age,gender,is_doctor,password=None):
        """Create a new userprofile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name=name,height=height,weight=weight,age=age,gender=gender,is_doctor=is_doctor)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name,height,weight,age,gender,is_doctor,password):
        user = self.create_user(email,name,height,weight,age,gender,is_doctor, password)

        user.is_superuser = True
        user.is_doctor= True
        user.is_staff=True
        user.save(using=self._db)

        return user
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database moedls for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50,choices = (("male","Male"),("female","Female")))
    date_added =models.DateTimeField(auto_now_add=True)
    is_doctor = models.BooleanField()
    is_staff = models.BooleanField(default=False)



    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','height','weight','age','gender','is_doctor']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class ProfileVitals(models.Model):
    """Store Vitals of User"""
    user_profile = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE

    )
    heart_rate = models.FloatField(default=-1)
    spo2 = models.FloatField(default=-1)
    breathing_rate = models.FloatField(default=-1)
    blood_pressure = models.CharField(max_length=15,default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    is_evaluated = models.BooleanField(default=False)
    assign_to = models.ForeignKey(UserProfile,default=None,on_delete=models.SET_NULL,null=True,related_name='doctor_id')

    def __str__(self):
        return str(self.id)
class ActualVitals(models.Model):
    """Store actual vitals of user for cross referencing"""
    user_profile = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
    )
    heart_rate = models.FloatField(default=-1)
    spo2 = models.FloatField(default=-1)
    breathing_rate = models.FloatField(default=-1)
    blood_pressure = models.CharField(max_length=15,default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    equipment = models.CharField(max_length=255,default=None)
    comments = models.CharField(max_length=255,default=None)

    def __str__(self):
        return str(self.id)
