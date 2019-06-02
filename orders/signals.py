# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404
from orders.models import ProductinBasket
from .models import Order
from importlib import import_module
from django.conf import settings

@receiver(post_save, sender=Order)
# def send_mail_on_create(sender, instance, created, **kwargs):
#     if created:
#         context = {
# 		    'order_name': instance.customer_name,
# 		    'order_number': instance.pk,
# 		    'order_edu': instance.education,
# 		    'contact_phone': instance.customer_phone,
# 		    'contact_email': instance.customer_email,
# 		}
#         subject = 'Заказ курса № edu-%s' % instance.pk
#         html_message = render_to_string('mail_templates/mail_template_eduorder.html', context)
#         plain_message = strip_tags(html_message)
#         from_email = 'info@likwid.club'
#         to = 'edu_orders@likwid.club'
#         if instance.is_emailed == False:
#             if subject and html_message and from_email:
#                 try:
#                     if send_mail(subject, plain_message, from_email, [to]):
#                         EducationOrder.objects.filter(pk=instance.pk).update(is_emailed=True)
#                         instance.is_emailed = True
#                 except BadHeaderError:
#                     return print('Invalid header found in email %s' % instance.pk)
#                 return print('email is sended %s' % instance.pk)
#             else:
#     	        return print('Make sure all fields are entered and valid %s' % instance.pk)

def update_products_in_basket_on_create(sender, instance, created, **kwargs):
    if created:
        SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
        s = SessionStore()
        session_key = s.session_key

        print(session_key)
        print(sender)
        print('sender')
        print(instance)
        print('instance')
        # print()
    pass
        # context = {
		#     'order_name': instance.customer_name,
		#     'order_number': instance.pk,
		#     'order_edu': instance.education,
		#     'contact_phone': instance.customer_phone,
		#     'contact_email': instance.customer_email,
		# }

        # subject = 'Заказ курса № edu-%s' % instance.pk
        # html_message = render_to_string('mail_templates/mail_template_eduorder.html', context)
        # plain_message = strip_tags(html_message)
        # from_email = 'info@likwid.club'
        # to = 'edu_orders@likwid.club'
        # if instance.is_emailed == False:
        #     if subject and html_message and from_email:
        #         try:
        #             if send_mail(subject, plain_message, from_email, [to]):
        #                 Order.objects.filter(pk=instance.pk).update(is_emailed=True)
        #                 instance.is_emailed = True
        #         except BadHeaderError:
        #             return print('Invalid header found in email %s' % instance.pk)
        #         return print('email is sended %s' % instance.pk)
        #     else:
    	#         return print('Make sure all fields are entered and valid %s' % instance.pk)
