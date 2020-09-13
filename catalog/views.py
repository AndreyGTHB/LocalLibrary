from django.shortcuts import render
from .models import *


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.all().filter(status__exact='a').count()
    num_authors = Author.objects.count()

    response = render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors}
    )
    return response


def book_list(request):
    num_books = Book.objects.count()
