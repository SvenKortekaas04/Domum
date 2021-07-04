from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import (
    FileSerializer,
    FolderSerializer,
    UploadFileSerializer,
    UserSerializer
)
from apps.core.util.storage import (
    create_file,
    create_folder,
    handle_uploaded_file
)
from apps.users.util import delete_user


class UsersView(APIView):
    """
    List all users.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    """
    Retrieve or delete a specific user.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        try:
            User = get_user_model()
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, username):
        user = self.get_object(username)

        # Delete a user
        delete_user(username=user.username)

        return Response(status=status.HTTP_204_NO_CONTENT)


class FileUploadView(APIView):
    """
    Upload a file.
    """

    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = UploadFileSerializer(request.POST, request.FILES)
        if serializer.is_valid(raise_exception=True):
            path = request.GET.get("path")  # Get path from query string

            for f in request.FILES.getlist("file"):
                handle_uploaded_file(request.user, f, path)

            return redirect("core_browse", request.user.storage_id, path)


class FilesView(APIView):
    """
    Get or create files.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get parameters
        name = request.POST.get("name")
        path = request.GET.get("path")

        # Create a new instance of the serializer
        serializer = FileSerializer(data={"name": name, "path": path})

        if serializer.is_valid(raise_exception=True):
            # Create file
            create_file(request.user, path, name)

            return redirect("core_browse", request.user.storage_id, path)


class FoldersView(APIView):
    """
    Get or create folders.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get parameters
        name = request.POST.get("name")
        path = request.GET.get("path")

        # Create a new instance of the serializer
        serializer = FolderSerializer(data={"name": name, "path": path})

        if serializer.is_valid(raise_exception=True):
            # Create folder
            create_folder(request.user, path, name)

            return redirect("core_browse", request.user.storage_id, path)