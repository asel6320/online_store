from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title', unique=True)
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name='Description')
    title_slug = models.SlugField(max_length=50, null=True, unique=True)
    def __str__(self):
        return f"{self.pk}. {self.title}"
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')
    category = models.ForeignKey("webapp.Category", on_delete=models.RESTRICT, verbose_name='Category', related_name='products', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Price")
    remainder = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Remainder')
    image_url = models.URLField(max_length=200, null=False, blank=False, verbose_name="Image")

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.description} - {self.category} - {self.created_at} - {self.price} - {self.image_url} -{self.remainder}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'