from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm, AuthorForm, RegistrationForm, LoginForm
from .filters import BookFilter
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_details.html', {'book': book})


@login_required
def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        author_form = AuthorForm(request.POST)
        if book_form.is_valid() and (author_form.is_valid() or book_form.cleaned_data['author']):
            if not book_form.cleaned_data['author']:
                author = author_form.save()
                book = book_form.save(commit=False)
                book.author = author
                book.save()
            else:
                book_form.save()
            return redirect('home')
    else:
        book_form = BookForm()
        author_form = AuthorForm()
    return render(request, 'add_book.html', {'book_form': book_form, 'author_form': author_form})


def books_list(request):
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'books_list.html', {'filter': book_filter})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
