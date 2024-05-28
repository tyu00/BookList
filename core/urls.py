from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_rating/<int:book_id>/', views.add_rating, name='add_rating'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('ratings/', views.ratings, name='ratings'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
