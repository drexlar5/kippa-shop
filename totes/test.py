from django.test import TestCase

from django.contrib.auth.models import User
from totes.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='PLAIN TOTES', slug='plain-totes')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'PLAIN TOTES')


    class TestProductsModel(TestCase):
        def setUp(self):
            Category.objects.create(name='PLAIN TOTES', slug='plain-totes')
            User.objects.create(username='admin')
            self.data1 = Product.objects.create(category_id=1, title='Denim Tote', created_by_id=1, slug='denim-tote',
                                                 price='2000.00', image='denim_tote')
            
        def test_products_model_entry(self):
            """
            Test Category model data insertion/types/field attributes
            """
            data = self.data1
            self.assertTrue(isinstance(data, Product))
            self.assertEqual(str(data), 'Denim Tote')
