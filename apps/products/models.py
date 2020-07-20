from django.db import models

from apps.common.models import TimeStampedModel
from apps.common.utils import unique_slug_generator


class Category(TimeStampedModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoría'
        verbose_name_plural = ('Categorías')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        super(Category, self).save(*args, **kwargs)


class Product(TimeStampedModel):
    name = models.CharField(max_length=32)
    slug = models.SlugField(blank=True, null=True)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        super(Product, self).save(*args, **kwargs)
