from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='borrowed-books'),
    path('books/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<pk>/refresh', views.refresh_book, name='book-refresh'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
