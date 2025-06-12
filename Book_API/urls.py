from django.urls import path

from .views import BookList, BookDetail, CreateBook, EditBook, AdminBookDetail, DeleteBook

app_name = 'Book_API'

# localhost:8000/api/v1/admin/create/

urlpatterns = [
    path('', BookList.as_view(), name='listbook'),
    path('book/<str:pk>/', BookDetail.as_view(), name='detailbook'),

    # Book Admin URLs
    path('admin/create/', CreateBook.as_view(), name='createbook'),
    path('admin/edit/bookdetail/<int:pk>/', AdminBookDetail.as_view(), name='admindetailbook'),
    path('admin/edit/<int:pk>/', EditBook.as_view(), name='editbook'),
    path('admin/delete/<int:pk>/', DeleteBook.as_view(), name='deletebook'),

]
