from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('announcements', views.announcements, name='announcements'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('postbook', views.postbook, name='postbook'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_search', views.book_search, name='book_search'),
    path('random_book', views.random_book, name='random_book'),
    path('wishlist', views.wishlist, name='wishlist')
]
