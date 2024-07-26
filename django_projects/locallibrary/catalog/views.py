from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from .constants import LOAN_STATUS
from django.views import generic
from .constants import PAGINATE_BY
from .constants import LOAN_STATUS_AVAILABLE 
# Create your views here.
def index(request):
  """View function for home page of site."""
  num_books = Book.objects.count()
  num_instances = BookInstance.objects.count()
  num_instances_available = BookInstance.objects.filter(status=LOAN_STATUS_AVAILABLE).count()
  num_authors = Author.objects.count()
  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
  }
  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)
class BookListView(generic.ListView):
      model = Book
      paginate_by = PAGINATE_BY
class BookDetailView(generic.DetailView):
      model = Book
def bookview(request):
    context = {
        'loan_status': dict(LOAN_STATUS),
    }
    return render(request, 'book_detail.html', context)
