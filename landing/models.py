# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from tinymce import HTMLField
from accounts.models import Profile


class Landpost(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField('Content')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост для лендинга'
        verbose_name_plural = 'Посты для лендинга'


class Callmecontact(models.Model):
    customer_name = models.CharField(verbose_name="ваше имя", max_length=32, default=None)
    customer_phone = PhoneNumberField(verbose_name="ваш телефон")
    referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.customer_name

    class Meta:
        verbose_name = 'Контакт для обратного звонка'
        verbose_name_plural = 'Контакты для обратного звонка'
        # app_label = 'landing'

    def save(self, *args, **kwargs):
        super(Callmecontact, self).save(*args, **kwargs)
