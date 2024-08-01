from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from .constants import LoanStatus
# Create your views here.
def index(request):
  """View function for home page of site."""
  num_books = Book.objects.count()
  num_instances = BookInstance.objects.count()
  num_instances_available = BookInstance.objects.filter(status=LoanStatus.AVAILABLE.value).count()
  num_authors = Author.objects.count()
  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
  }
  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)
