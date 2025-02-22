from django.db import models

# Create your models here.
      
class UserRegistration(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = "user_registration"

class Profile(models.Model):
    user = models.OneToOneField(UserRegistration, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/', max_length=100)

    class Meta:
        db_table = "profile"