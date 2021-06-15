from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        "store.Category", on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_on')

    def __str__(self):
        return self.title
