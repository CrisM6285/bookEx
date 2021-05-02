from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import MainMenu
from .models import Announcement
from .models import Book
from .models import Wish
from .forms import AnnouncementForm, SearchForm, WishForm, BookForm

from random import randint


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'title': "Home",
                      'header': "Welcome to Book Exchange System",
                      'item_list': MainMenu.objects.all()
                  })


def announcements(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.username = request.user
            a.save()
            return HttpResponseRedirect('/announcements')
    else:
        form = AnnouncementForm()

    return render(request,
                  'bookMng/announcements.html',
                  {
                      'title': "Announcements",
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'announces': Announcement.objects.all()
                  })


def aboutus(request):
    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'title': "About Us",
                      'item_list': MainMenu.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                  {
                      'title': "Post Book",
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'title': "Display Books",
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


def wishlist(request):
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.theUser = request.user
            a.save()
            return HttpResponseRedirect('/wishlist')
    else:
        form = WishForm()
    return render(request,
                  'bookMng/wishlist.html',
                  {
                    'title': "Wish List",
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'wish_list': Wish.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'title': "My Books",
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'title': "Book Details",
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'title': "Book Delete",
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


@login_required(login_url=reverse_lazy('login'))
def book_search(request, searched=""):

    submitted = False
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.name = request.POST.get('name')
            return HttpResponseRedirect('/book_search?q=' + a.name)
    else:
        form = SearchForm()
        if 'q' in request.GET:
            searched = request.GET.get('q', '')
            submitted = True

    books = Book.objects.filter(name__icontains=searched)
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request, 'bookMng/book_search.html',
                  {
                      'title': "Book Search",
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'submitted': submitted,
                      'form': form,
                      'searched': searched
                  })


@login_required(login_url=reverse_lazy('login'))
def random_book(request):

    num_of_books = Book.objects.count()
    ran = randint(1, num_of_books) - 1

    book = Book.objects.all()[ran]
    book.pic_path = book.picture.url[14:]

    return render(request, 'bookMng/random_book.html',
                  {
                      'title': "Random Book",
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


class Register(CreateView):

    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
