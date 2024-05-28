from django.contrib import admin
from .models import Book, Author, Genre, User, Rating, Review, Bookmark


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Bookmark)
