from django.db import models
import re
import bcrypt
from .models import *

class RegisterManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first']) < 2:
            errors["first"] = "First name has to be at least 2 characters"
        if len(postData['last']) < 2:
            errors["last"] = "Last name has to be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']=("Invalid email address")
        if len(postData['password']) < 8:
            errors["password"] = "Password has to be at least 8 characters"
        if (postData['password']) != (postData['confirm']):
            errors["confirm"] = "Passwords should match"
        return errors 
    def login_validator(self, postData):
        errors = {}
        LoginUser = Register.objects.filter(email=postData['loginemail'])
        if len(LoginUser) > 0:
            if bcrypt.checkpw(postData['loginpassword'].encode(), LoginUser[0].password.encode()):
                print("Password matches")
            else:
                errors['loginpassword']="Incorrect password"
        else:
            errors['loginemail']="email does not exist"
        return errors

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['message']) < 1:
            errors['message'] = "Message has to be at least 1 character."
        return errors

class Register(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegisterManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Register, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(Register, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

