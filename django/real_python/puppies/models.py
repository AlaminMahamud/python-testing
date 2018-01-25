from django.db import models


class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return "{name} belongs to {breed} breed." \
            .format(
                name=self.name,
                breed=self.breed
            )

    def __repr__(self):
        return "{name} is added.".format(name=self.name)
