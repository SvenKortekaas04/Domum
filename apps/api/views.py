import shutil

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.api.serializers import UserSerializer
from apps.users.models import User


class UsersView(APIView):
    """
    List all users.
    """

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    """
    Retrieve or delete a specific user.
    """

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()

        # Delete storage
        shutil.rmtree(user.storage_path)

        return Response(status=status.HTTP_204_NO_CONTENT)

