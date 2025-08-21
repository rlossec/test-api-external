
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('EN', 'Engineering'),
        ('SA', 'Sales'),
        ('MK', 'Marketing'),
        ('HR', 'HR'),
        ('FI', 'Finance'),
        ('OP', 'Operations'),
        ('DE', 'Design')
    ]

    ROLE_CHOICES = [
        ('AD', 'Admin'),
        ('MA', 'Manager'),
        ('EM', 'Employee'),
    ]

    STATUS_CHOICES = [
        ('AC', 'Active'),
        ('IN', 'Inactive'),
        ('RE', 'Removed'),
    ]

    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
