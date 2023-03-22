from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/results')

class BioData(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    developer_no = models.CharField(max_length=10)
    level = models.IntegerField()
    degree = models.CharField(max_length=5)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    course_code = models.CharField(null=True, blank=True, max_length=30)
    course_title = models.CharField(null=True, blank=True, max_length=150)
    units = models.IntegerField(null=True, blank=True,)
    status = models.CharField(null=True, blank=True, max_length=1)
    level = models.IntegerField(null=True, blank=True)
    checkbox = models.BooleanField(null=True,)

    def __str__(self):
        return self.course_code

class Registered(models.Model):
    name = models.CharField(null=True, max_length=30)

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DateTimeField()

class Application(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
