from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Custom User model inheriting from AbstractUser

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
