from django.db import models


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
    category = models.ForeignKey("store.Category", on_delete=models.CASCADE, related_name='product')
    