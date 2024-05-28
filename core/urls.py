from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('add_book/', views.add_book, name='add_book'),
]