from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


# initialize the APIClient app
client = Client()


class GetAllPuppiesTest(TestCase):

    """
    Test Module for GET all puppies API
    """

    def setUp(self):
        Puppy.objects.create(
            name='Casper',
            age=3,
            breed='Bull Dog',
            color='Black'
        )
        Puppy.objects.create(
            name='Muffin',
            age=1,
            breed='Graddane',
            color='Brown'
        )
        Puppy.objects.create(
            name='Ricky',
            age=5,
            breed='Something',
            color='Pink'
        )

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppies'))

        # get data from db
        puppies = Puppy.objects.all()

        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
