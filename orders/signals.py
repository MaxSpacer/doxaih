# -*- coding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404
# from orders.models import
from .models import ProductinBasket, Order
from importlib import import_module
from django.conf import settings

@receiver(post_save, sender=Order)
def update_products_in_basket_on_create(sender, instance, created, **kwargs):
    if created:
        products_in_basket = ProductinBasket.objects.filter(pb_session_key=instance.order_session_key, pb_is_active=True)
        for items in products_in_basket:
            items.pb_order = instance
            items.pb_session_key = None
            print(instance)
            print(items)
            items.save()


        context = {
		    'order_name': instance.customer_name,
		    'order_number': instance.pk,
		    'order_adress': instance.customer_adress,
		    'contact_phone': instance.customer_phone,
		    'contact_comments': instance.customer_comments,
		    'total_price_order': instance.total_price_order,
		    # 'basket_order': instance,
		}
        context["basket_order"] = list()
        for item in products_in_basket:
            product_dict = dict()
            # product_dict["id"] = item.id
            product_dict["product_name"] = item.pb_product.name
            product_dict["price_per_item"] = item.pb_price_per_item
            product_dict["numb"] = item.pb_qty
            product_dict["total_price"] = item.pb_total_price
            # product_dict["products_in_basket_total_price"] = item.pb_total_price
            context["basket_order"].append(product_dict)


        print(products_in_basket)
        print(context)
        subject = 'Заказ № %s' % instance.pk
        html_message = render_to_string('mail_templates/mail_template_eduorder.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'info@doxaih.ru'
        to = 'zakaz@doxaih.ru'
        if instance.is_emailed == False:
            if subject and html_message and from_email:
                try:
                    if send_mail(subject, plain_message, from_email, [to], html_message=html_message):
                        Order.objects.filter(pk=instance.pk).update(is_emailed=True)
                        instance.is_emailed = True
                except BadHeaderError:
                    return print('Invalid header found in email %s' % instance.pk)
                return print('email is sended %s' % instance.pk)
            else:
    	        return print('Make sure all fields are entered and valid %s' % instance.pk)

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
