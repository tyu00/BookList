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
]
