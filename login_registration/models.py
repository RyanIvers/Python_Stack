from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Name must be at least 1 character"
        
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Name must be at least 1 character"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        user_list = User.objects.filter(email = postData['email'])
        if len(user_list) > 0:
            errors['email'] = "Account with that email already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"       

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)