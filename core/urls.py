from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('add_book/', views.add_book, name='add_book'),
    path('search/', views.books_list, name='books_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('book/<int:book_id>/add-bookmark/', views.add_bookmark, name='add_bookmark'),
    path('bookmarks/remove/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('bookmarks/', views.user_bookmarks, name='user_bookmarks'),
    path('bookmarks/change/<int:bookmark_id>/', views.change_bookmark_status, name='change_bookmark_status'),
]
