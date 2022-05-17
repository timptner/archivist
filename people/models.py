from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
