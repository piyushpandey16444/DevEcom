from django.test import TestCase
from store.models import Product, Category


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
