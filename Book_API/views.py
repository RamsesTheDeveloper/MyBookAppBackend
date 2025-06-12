from Book.models import Book
from .serializers import BookSerializer

from rest_framework import generics, viewsets, filters, permissions, status
from rest_framework.views import APIView

from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Custom Permission
class BookUserWritePermission(BasePermission):
    message = 'Editing books is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

# Create your views here.
# - Display Books -

# Return All Books

class BookList(generics.ListAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

# Return Specifc Book via slug
class BookDetail(generics.RetrieveAPIView):
    serializer_class = BookSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Book, slug=item)

# Note that slug can be substituted for id.

# - Book Admin -

class CreateBook(APIView):
    # permission_classes = [permissions.AllowAny] # PracticeiOS
    permission_classes = [permissions.IsAuthenticated] # MyBookApp

    def post(self, request, format=None):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminBookDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.AllowAny] # PracticeiOS
    permission_classes = [permissions.IsAuthenticated] # MyBookApp
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class EditBook(generics.UpdateAPIView):
    # permission_classes = [permissions.AllowAny] # PracticeiOS
    permission_classes = [permissions.IsAuthenticated] # MyBookApp
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBook(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.AllowAny] # PracticeiOS
    permission_classes = [permissions.IsAuthenticated] # MyBookApp
    serializer_class = BookSerializer
    queryset = Book.objects.all()