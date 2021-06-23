from django.contrib.auth.models import User
from django.db import models


class UserEmail(models.Model):
    email = models.CharField(verbose_name='Email', max_length=100, unique=True)
    phone = models.CharField(verbose_name='Phone number', max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    text = models.TextField(verbose_name='Comment', blank=True)

    class Meta:
        verbose_name_plural = 'Email'
        verbose_name = 'Email Object'
