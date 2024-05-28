from django.shortcuts import render, redirect
from .models import Book, Author, Genre
from .forms import BookForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


# Представление для входа
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


# Представление для выхода
def logout_view(request):
    logout(request)
    return redirect('home')


# Представление для регистрации
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Представление для главной страницы
def home(request):
    books = Book.objects.all().order_by('-publication_date')
    return render(request, 'home.html', {'books': books})


# Представление для деталей книги
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_details.html', {'book': book})


# Представление для добавления книги
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# Представление для добавления оценки
@login_required
def add_rating(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.book = book
            rating.user = request.user
            rating.save()
            return redirect('book_details', book_id=book_id)
    else:
        form = RatingForm()
    return render(request, 'add_rating.html', {'form': form, 'book': book})


# Представление для закладок пользователя
@login_required
def bookmarks(request):
    user_bookmarks = Book.objects.filter(bookmarks__user=request.user)
    return render(request, 'bookmarks.html', {'bookmarks': user_bookmarks})


# Представление для оценок пользователя
@login_required
def ratings(request):
    user_ratings = Book.objects.filter(ratings__user=request.user)
    return render(request, 'ratings.html', {'ratings': user_ratings})
