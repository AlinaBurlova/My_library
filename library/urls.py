from django.urls import path
from .views import index, about, add_book, book_list, book_detail, book_edit, book_delete

app_name = 'library'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('books/add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
    path('books/<slug:slug>/', book_detail, name='book_detail'),
    path('books/<slug:slug>/edit', book_edit, name='book_edit'),
    path('books/<slug:slug>/delete', book_delete, name='book_delete'),
]
