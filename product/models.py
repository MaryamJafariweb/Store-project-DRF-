from django.db import models
from django.urls import reverse


# Create your models here.

class ProductCategories(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='category')
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug])


class ProductBrand(models.Model):
    name = models.CharField(max_length=300)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    category = models.ManyToManyField(ProductCategories)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='image/product', null=True, blank=True)
    image2 = models.ImageField(upload_to='image/product', null=True, blank=True)
    image3 = models.ImageField(upload_to='image/product', null=True, blank=True)
    price = models.IntegerField()
    short_description = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField()
    offer = models.BooleanField(blank=True, null=True)
    featured = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name} ({self.price})"


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return f'{self.email}-{self.body[:20]}'



