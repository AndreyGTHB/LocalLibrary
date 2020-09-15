from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class BookListView(ListView):
    model = Book
    paginate_by = 15

    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book

    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class AuthorListView(ListView):
    model = Author

    context_object_name = 'author_list'
    template_name = 'authors/author_list.html'

class AuthorDetailView(DetailView):
    model = Author

    context_object_name = 'author'
    template_name = 'authors/author_detail.html'


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    response = render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors}
    )
    return response

