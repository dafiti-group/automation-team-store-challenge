from django.test import TestCase
from .models import WomenShoes


class WomenShoesTest(TestCase):
    """ Test module for WomenShoes model """

    def setUp(self):
        
        WomenShoes.objects.create(
            brand='Usaflex',
            colors='Black',
            count=5,
            dateAdded='2021-04-21T05:23:00Z',
            dateUpdated='2021-04-21T05:23:00Z',
            manufacturer='Usaflex',
            name='Sapatilha Preta',
            price=23.56,
            weight=1
        )
        
        WomenShoes.objects.create(
            brand='Moleca',
            colors='Pink,Silver',
            count=5,
            dateAdded='2021-04-21T05:23:00Z',
            dateUpdated='2021-04-21T05:23:00Z',
            manufacturer='Moleca',
            name='Sapatilha Baixa',
            price=49.90,
            weight=1
        )

    def test_women_shoe_manufacturer(self):
        women_shoe_usaflex = WomenShoes.objects.get(name='Sapatilha Preta')
        women_shoe_moleca = WomenShoes.objects.get(name='Sapatilha Baixa')
        self.assertEqual(
            women_shoe_usaflex.get_shoe(), 'Sapatilha Preta is from manufacturer Usaflex')
        self.assertEqual(
            women_shoe_moleca.get_shoe(), 'Sapatilha Baixa is from manufacturer Moleca')
