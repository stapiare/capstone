from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = (
        ('invitado','Invitado'),
        ('adminsitrador','Administrador'),
        ('tutor','Tutor'),
        ('estudiandte','Estudiante'),
    )

    nombre = models.CharField(max_length = 100, blank=True, null = True)
    apellido = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(max_length=255, unique=True)
    tipo = models.CharField(max_length=100,blank=True, null=True, choices=TIPO_CHOICES, default='NONE')