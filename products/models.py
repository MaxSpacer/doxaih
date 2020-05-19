from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField('Имя категории проукции',max_length=64, blank=True, null=True, default=None)
    order_sort = models.PositiveSmallIntegerField('Порядок сортировки', blank=True, null=True, default=None)
    is_active = models.BooleanField('активен?', default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукции'


class Product(models.Model):

    Gramms = 'гр.'
    Nums = 'шт.'
    Vol = 'л.'

    VOLUME_TYPE_CHOICES = [
        (Gramms, 'Граммы'),
        (Nums, 'Штуки'),
        (Vol, 'Литры')
    ]
    name = models.CharField('имя продукции', max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None, verbose_name='категория продукции')
    price = models.DecimalField('цена за шт.', max_digits=10, decimal_places=0, default=0)
    weight = models.IntegerField('вес',default=0)
    volume_type = models.CharField('мера количества', max_length=4,choices=VOLUME_TYPE_CHOICES,default=Gramms)
    description = models.TextField('описание', blank=True, null=True, default=None)
    popular = models.BooleanField('популярные товары', default=False)
    pref_category = models.BooleanField('Представитель категории', default=False)
    is_active = models.BooleanField('активен?',default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, verbose_name='продукт')
    image = models.ImageField('Фото для продукта',upload_to='product_images/')
    is_main = models.BooleanField('Главная картинка?',default=False)
    is_active = models.BooleanField('активен?',default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.image

    class Meta:
        verbose_name = 'Фотография продукции'
        verbose_name_plural = 'Фотографии продукции'
