from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        """
        Creating provie objects
        """
        usr1 = User.objects.create(username="Anne", email="a@mail.fr")
        usr2 = User.objects.create(username="Ben", email="b@mail.fr")
        Profile.objects.create(favorite_city="St Denis", user=usr1)
        Profile.objects.create(favorite_city="Strasbourg", user=usr2)

    def test_profile_creation(self):
        """
        Testing the profile's data
        """
        p1 = Profile.objects.get(user__email="a@mail.fr")
        p2 = Profile.objects.get(user__email="b@mail.fr")
        self.assertEqual(p1.favorite_city, "St Denis")
        self.assertEqual(p1.user.username, "Anne")
        self.assertEqual(p2.favorite_city, "Strasbourg")
        self.assertEqual(p2.user.username, "Ben")


class HttpResponseTest(TestCase):
    def setUp(self):
        """
        Creating provie objects
        """
        usr1 = User.objects.create(username="Anne", email="a@mail.fr")
        usr2 = User.objects.create(username="Ben", email="b@mail.fr")
        Profile.objects.create(favorite_city="St Denis", user=usr1)
        Profile.objects.create(favorite_city="Strasbourg", user=usr2)

    def test_profile_home_page(self):
        """
        Testing the url to profile page
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Profiles", response.content)
        self.assertIn(b"Anne", response.content)
        self.assertIn(b"Ben", response.content)

    def test_letting_page(self):
        """
        Testing the url to profile page
        """
        response = self.client.get('/profiles/Anne/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Email :", response.content)
        self.assertIn(b"a@mail.fr", response.content)
        self.assertNotIn(b"b@mail.fr", response.content)
