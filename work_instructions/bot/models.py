from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Activity(models.Model):
    chat_id = models.IntegerField()
    type = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class User(AbstractUser):
    GENDER_CHOICES = (
        ('backend', 'BACKEND'),
        ('frontend', 'FRONTEND'),
        ('seo', 'SEO'),
        ('ui_ux', 'UI|UX DESIGNER')
    )
    telegram_id = models.CharField(max_length=64, default='')
    stack = models.CharField(choices=GENDER_CHOICES, max_length=64)
    phone_number = models.CharField(max_length=9, default=0)

    def __str__(self):
        return self.username


class Task(models.Model):
    GENDER_CHOICES = (
        ('started', 'STARTED'),
        ('late_submitted', 'LATE SUBMITTED'),
        ('completed', 'COMPLETED')
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=125, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    status = models.CharField(choices=GENDER_CHOICES, max_length=64, default='started')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user_id.username


class Problem(models.Model):
    TYPE_CHOICES = (
        ('critical', 'CRITICAL'),
        ('high', 'HIGH'),
        ('medium', 'MEDIUM'),
        ('low', 'LOW')
    )
    completed_choices = (
        ('completed', 'COMPLETED'),
        ('not_completed', 'NOT COMPLETED'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=125, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=64, blank=True, null=True)
    completed = models.CharField(max_length=64, choices=completed_choices, default='not_completed')
    created_date = models.DateTimeField(auto_created=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Bug(models.Model):
    GENDER_CHOICES = (
        ('fixed_bug', 'FIXED BUG'),
        ('not_fixed_bug', 'NOT FIXED BUG'),
    )
    TYPE_CHOICES = (
        ('critical', 'CRITICAL'),
        ('high', 'HIGH'),
        ('medium', 'MEDIUM'),
        ('low', 'LOW')
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.CharField(max_length=125, blank=True, null=True)
    priority = models.CharField(max_length=64, choices=TYPE_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=64, choices=GENDER_CHOICES, default='not_fixed_bug')

