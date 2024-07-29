from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
  """View function for home page of site."""
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.count()
    # Number of visits to this view, as counted in the session variable.
  num_visits = request.session.get('num_visits', 1)
  request.session['num_visits'] = num_visits + 1
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
      paginate_by = 10
class BookDetailView(generic.DetailView):
      model = Book
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Lớp view liệt kê các sách đang mượn bởi người dùng hiện tại."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')