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
