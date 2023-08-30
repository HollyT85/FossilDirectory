from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rock
from .serializers import RockSerializer


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