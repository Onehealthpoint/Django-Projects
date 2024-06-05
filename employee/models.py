from django.db import models
from django.contrib.auth.models import User


class EmployeeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50)
    employee_dept = models.CharField(max_length=50, null=True)
    contacts = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    joining_date = models.DateField(null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    passing_year = models.IntegerField()
    score = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class EmployeeCareer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    leaving_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username
