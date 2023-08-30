from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rock
from .serializers import RockSerializer
from fossil_api.permissions import IsOwnerOrReadOnly


class RockList(APIView):
    serializer_class = RockSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        rocks = Rock.objects.all()
        serializer = RockSerializer(
            rocks, many=True, context={'request':request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RockSerializer(
            data=request.data, context={'request':request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

def RockDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RockSerializer

    def get_object(self, pk):
        try:
            rock = Rock.objects.get(pk=pk)
            self.check_object_permissions(self.request, rock)
            return rock
        except Rock.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rock = self.get_object(pk)
        serializer = RockSerializer(
            rock, context={'request':request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        rock = self.get_object(pk)
        serializer = RockSerializer(
            rock, data=request.data, context={'request':request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializers.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        rock = self.get_object(pk)
        rock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)