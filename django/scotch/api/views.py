from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import BucketList


class CreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()
