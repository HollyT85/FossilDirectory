from rest_framework import generics, permissions
from fossil_api.permissions import IsOwnerOrReadOnly
from .models import RockComments
from .serializers import RockCommentSerializer, RockCommentDetailSerializer


class RockCommentList(generics.ListCreateAPIView):

    serializer_class = RockCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RockComments.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RockCommentDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RockCommentDetailSerializer
    queryset = RockComments.objects.all()