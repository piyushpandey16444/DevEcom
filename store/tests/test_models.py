from django.test import TestCase
from store.models import Product, Category
from django.contrib.auth.models import User


class TestCategory(TestCase):

    def setUp(self):
        """
        Use to create data for testing
        """
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProduct(TestCase):

    def setUp(self):
        category = Category.objects.create(name='django', slug='django')
        user = User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=category.id, title='django basics', created_by_id=user.id, slug='django-basics', price='20.00', image='django')

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django basics')
