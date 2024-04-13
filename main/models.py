from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=0)
    ability = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self) -> str:
        return self.name