import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)  # Make email field unique
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Provide unique related names for user_groups and user_permissions fields
        # to avoid clash with the default User model's groups and user_permissions fields
        # Ensure these related names are unique and not clashing with other fields in your models
        db_table = 'custom_user'
        permissions = (("can_vote", "Can vote in polls"),)
        default_permissions = ['view', 'add', 'change', 'delete']
        swappable = 'AUTH_USER_MODEL'
