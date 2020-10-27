from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class BookListView(ListView):
    model = Book
    paginate_by = 10

    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class AuthorListView(ListView):
    model = Author
    paginate_by = 10

    context_object_name = 'author_list'
    template_name = 'authors/author_list.html'


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author

    context_object_name = 'author'
    template_name = 'authors/author_detail.html'


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance

    template_name = 'books/loaned_books_by_user_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    response = render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors}
    )
    return response






