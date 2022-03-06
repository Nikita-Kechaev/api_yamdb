from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLE = 'user'
ADMIN_ROLE = 'admin'
MODERATOR_ROLE = 'moderator'


class User(AbstractUser):
    ROLE = (
        (USER_ROLE, 'user'),
        (ADMIN_ROLE, 'admin'),
        (MODERATOR_ROLE, 'moderator'),
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=50, choices=ROLE, default=USER_ROLE)

    @property
    def is_admin(self):
        return self.role == ADMIN_ROLE or self.is_staff

    @property
    def is_moderator(self):
        return self.role == MODERATOR_ROLE
