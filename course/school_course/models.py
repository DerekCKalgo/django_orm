from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name'])<6:
            errors["name"] = "Name has to have more than 5 characters"
        if len(postData['desc'])<16:
            errors["description"] = "Description has to have more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

