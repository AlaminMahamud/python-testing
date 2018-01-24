# general imports
from django.test import TestCase

# import for model testing
from .models import BucketList

# import for serializers testing

# import for viewset testing
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class TestBucketList(TestCase):
    """
    Summary:
    -------
    testcases for BucketList Model

    Description:
    ------------
    BucketList contains only name, created, and updated fields

    Behaviours:
    ------------
    1. BucketList can create a new list

    """

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.bucketlist_name = "World Class"
        self.bucketlist = BucketList(name=self.bucketlist_name)

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_model_can_create_a_bucketlist(self):
        """
        Summary:
        ---------
        sets published at to given date


        Description:
        ------------
        extended summary

        """
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)


class TestBucketListView(TestCase):
    """
    Test Suite for the api views
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """
        Define the test client and other test variables
        """
        self.client = APIClient()
        self.bucketlist_data = {
            'name': 'Goto Ibiza'
        }
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json'
        )

    def tearDown(self):
        pass

    def test_api_can_create_a_bucketlist(self):
        """
        """
        self.assertEqual(
            self.response.status_code,
            status.HTTP_201_CREATED
        )

    def test_api_can_get_a_bucketlist(self):
        """
        """
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse(
                'details',
                kwargs={
                    'pk': bucketlist.id
                }
            ),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_a_bucketlist(self):
        change_bucketlist = {
            'name': 'something new'
        }
        bucketlist = BucketList.objects.get()
        res = self.client.put(
            reverse(
                'details',
                kwargs={
                    'pk': bucketlist.id
                }
            ),
            change_bucketlist,
            format="json"
        )

        self.assertEqual(
            res.status_code,
            status.HTTP_200_OK
        )

    def test_api_can_delete_bucketlist(self):
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
