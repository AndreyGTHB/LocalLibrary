import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import BookRefreshForm
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

    template_name = 'books/loaned_books_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        books = BookInstance.objects.filter(status__exact='o')
        if not self.request.user.has_perm('catalog.librarian'):
            books = books.filter(borrower=self.request.user)
        return books.order_by('due_back')


@permission_required('catalog.librarian')
def refresh_book(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = BookRefreshForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('borrowed-books'))
    else:
        default_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = BookRefreshForm({'renewal_date': default_renewal_date})
    return render(request, 'books/book_refresh_form.html', {'form': form, 'book_inst': book_inst})


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






