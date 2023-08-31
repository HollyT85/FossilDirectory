from django.http import Http404
from rest_framework import filters, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rock
from .serializers import RockSerializer
from fossil_api.permissions import IsOwnerOrReadOnly


class RockList(generics.ListCreateAPIView):

    serializer_class = RockSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Rock.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = [
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RockDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = RockSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rock.objects.all()