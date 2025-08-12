from django.test import TestCase
from lettings.models import Address, Letting


class AddressTestCase(TestCase):
    def setUp(self):
        """
        Creating address objects
        """
        Address.objects.create(number=7, street="Bd de la Victoire",
                               city="Strasbourg", state="France",
                               zip_code=67000, country_iso_code="3166-2:FR")
        Address.objects.create(number=1, street="Piazzale Loreto",
                               city="Milano", state="Italy", zip_code=20127,
                               country_iso_code="3166-1:alpha-2")

    def test_address_creation(self):
        """
        Testing the datas of adresses created
        """
        ad1 = Address.objects.get(number=7)
        ad2 = Address.objects.get(number=1)
        self.assertEqual(ad1.street, "Bd de la Victoire")
        self.assertEqual(ad1.city, "Strasbourg")
        self.assertEqual(ad1.zip_code, 67000)
        self.assertEqual(ad1.country_iso_code, "3166-2:FR")
        self.assertEqual(ad2.street, "Piazzale Loreto")
        self.assertEqual(ad2.zip_code, 20127)
        self.assertEqual(ad2.state, "Italy")

    def test_letting(self):
        ad = Address.objects.get(number=1)
        ad2 = Address.objects.get(number=7)
        letting1 = Letting.objects.create(title="We hunged Mussolini here",
                                          address=ad)
        letting2 = Letting.objects.create(title="The Tram is still there",
                                          address=ad2)
        self.assertEqual(letting1.title, "We hunged Mussolini here")
        self.assertEqual(letting1.address.city, "Milano")
        self.assertEqual(letting2.title, "The Tram is still there")
        self.assertEqual(letting2.address.country_iso_code, "3166-2:FR")


class HttpResponseTest(TestCase):
    def setUp(self):
        """
        Creating address and letting objects
        """
        ad1 = Address.objects.create(number=7, street="Bd de la Victoire",
                                     city="Strasbourg", state="France",
                                     zip_code=67000, country_iso_code="3166-2:FR")
        ad2 = Address.objects.create(number=1, street="Piazzale Loreto",
                                     city="Milano", state="Italy", zip_code=20127,
                                     country_iso_code="3166-1:alpha-2")
        Letting.objects.create(title="We hunged Mussolini here",
                               address=ad2)
        Letting.objects.create(title="The Tram is still there",
                               address=ad1)


    def test_letting_home_page(self):
        """
        Testing the url to profile page
        """
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lettings", response.content)
        self.assertIn(b"We hunged Mussolini here", response.content)
        self.assertIn(b"The Tram is still there", response.content)

    def test_letting_page(self):
        """
        Testing the url to profile page
        """
        l = Letting.objects.get(address__number=7)
        response = self.client.get(f'/lettings/{l.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lettings", response.content)
        self.assertNotIn(b"We hunged Mussolini here", response.content)
        self.assertIn(b"The Tram is still there", response.content)
        self.assertIn(b"France", response.content)
