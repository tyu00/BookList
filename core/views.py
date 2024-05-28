from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Bookmark, Rating
from .forms import BookForm, RatingForm, BookmarkForm
from .forms import ReviewForm


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_details.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def add_rating(request, book_id):
    book = get_object_or_404(Book, id=book_id)
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


def bookmarks(request):
    user_bookmarks = request.user.bookmarks_created.all()
    return render(request, 'bookmarks.html', {'bookmarks': user_bookmarks})


def bookmark(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, book=book)
    if not created:
        bookmark.delete()
    return redirect('book_details', book_id=book_id)


def ratings(request):
    user_ratings = request.user.ratings_given.all()
    return render(request, 'ratings.html', {'ratings': user_ratings})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'core/add_review.html', {'form': form, 'book': book})
