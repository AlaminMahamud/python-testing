from django.test import TestCase
from .models import BucketList


class TestBucketList(TestCase):
    """
    Summary:
    -------


    Description:
    ------------


    Behaviours:
    ------------
    1. sets published at to given date
    2. emits post_published event with post id
    3. does nothing for published posts

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
