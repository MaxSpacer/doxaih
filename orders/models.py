from django.db import models
from django.db.models.signals import post_save
from products.models import Product
from deployutils.main import disable_for_loaddata
from phonenumber_field.modelfields import PhoneNumberField


class Status_order(models.Model):
    status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    customer_name = models.CharField(verbose_name="ваше имя", max_length=64, blank=False, null=True, default=None)
    customer_phone = PhoneNumberField(verbose_name="ваш телефон", blank=False, null=True, default=None)
    customer_adress = models.TextField(verbose_name="адрес доставки", blank=False, null=True, default=None)
    customer_comments = models.TextField(verbose_name="комментарии к заказу", blank=True, null=True, default=None)
    total_price_order = models.DecimalField(verbose_name = 'общая сумма заказа', max_digits=10, decimal_places=2, default=0) #total_price in order for all products
    status = models.ForeignKey(Status_order, on_delete=models.SET_DEFAULT, default=1, verbose_name = 'статус заказа')
    is_emailed = models.BooleanField(default=False)
    order_session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "Заказ № %s %s" % (self.id, self.status.status_name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

# post_save.connect(product_in_order_post_save, sender=ProductinOrder)


class ProductinBasket(models.Model):
    pb_order = models.ForeignKey(Order, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, verbose_name = 'заказ')
    pb_product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, verbose_name = 'продукт')
    pb_qty = models.IntegerField(default=1, verbose_name = 'Кол-во')
    pb_price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name = 'цена товара')
    pb_total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name = 'общая сумма') #price*qty
    pb_is_active = models.BooleanField(default=True, verbose_name = 'активен?')
    pb_created = models.DateTimeField(auto_now_add=True , auto_now=False)
    pb_updated = models.DateTimeField(auto_now_add=False , auto_now=True)
    pb_session_key = models.CharField(max_length=128, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return "%s" % self.pb_product

    def save(self, *args, **kwargs):
        if self.pb_product.price:
            price_per_item = self.pb_product.price
            self.pb_price_per_item = price_per_item
            self.pb_total_price = int(self.pb_qty) * self.pb_price_per_item
        super(ProductinBasket, self).save(*args, **kwargs)
