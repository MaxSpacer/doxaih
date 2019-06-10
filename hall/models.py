# -*- coding: utf-8 -*-

from django.db import models


class Preference(models.Model):
    number_phone = models.CharField("номер телефона",max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.number_phone

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
