from django.db import models

# Create your models here.


class BucketList(models.Model):
    """
    This class represents the bucketlist model
    """
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{name}".format(name=self.name)
