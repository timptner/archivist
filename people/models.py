from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    FACULTIES = [
        ('MB', _('Mechanical Engineering')),
        ('VST', _('Process and Systems Engineering')),
        ('EIT', _('Electrical Engineering and Information Technology')),
        ('IN', _('Computer Science')),
        ('MA', _('Mathematics')),
        ('NW', _('Natural Sciences')),
        ('ME', _('Medicine')),
        ('HW', _('Humanities, Social Sciences and Education')),
        ('WW', _('Economics and Management')),
    ]
    faculty = models.CharField(_('Faculty'), max_length=3, choices=FACULTIES, null=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
