from django.contrib.auth.models import User, Group
from django.db import models
from django.conf import settings

# Task model to store task-related information


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('U', 'Urgent'),
        ('A', 'Asap'),
    ]
    CATEGORY_CHOICES = [
        ('W', 'Work'),
        ('P', 'Personal'),
        ('O', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default='M')
    category = models.CharField(
        max_length=1, choices=CATEGORY_CHOICES, default='O')

    def __str__(self):
        return self.title

# Profile model to store user profile information


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
# Check if the user is a member of a specific group


def is_member_of_group(self_name):
    return self.groups.filter(name=group_name).exists()


User.add_to_class("is_member_of_group", is_member_of_group)
