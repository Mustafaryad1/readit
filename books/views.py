from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import View, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from .models import Book, Author
from .forms import ReviewForm, BookForm


# Create your views here.

def list_books(request):
    """
    :param request:
    :return: response HTML with data
    """
    books = Book.objects.exclude(date_review__isnull=True).prefetch_related('authors')
    context = {
        'books': books
    }
    return render(request, 'list.html', context)


class AuthorList(View):
    def get(self, request):
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors
        }

        return render(request, 'author_list.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = 'book.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_details.html'


class ReviewList(View):
    def get(self, request):
        books = Book.objects.filter(date_review__isnull=True).prefetch_related('authors')
        form = BookForm()
        context = {
            'books': books,
            'form': form,
        }

        return render(request, "list-to-review.html", context)

    def post(self, request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_review__isnull=True).prefetch_related('authors')
        if form.is_valid():
            form.save()
            return redirect("review-books")
        context = {
            'books': books,
            'form': form
        }
        return render(request, "list-to-review.html", context)


@login_required()
def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book.is_favorite = form.cleaned_data['is_favorite']
            book.review = form.cleaned_data['review']
            book.reviewed_by = request.user
            book.save()
            return redirect("review-books")
    else:
        form = ReviewForm()
    context = {
        'book': book,
        'form': form
    }

    return render(request, "review-book.html", context)


class CreateAuthor(CreateView):
    model = Author
    fields = ['name', ]
    template_name = 'create-author.html'

    def get_success_url(self):
        return reverse('review-books')
