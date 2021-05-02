from django import forms
from django.forms import ModelForm

from .models import Announcement
from .models import Book
from .models import Wish
from .models import BookSearch


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class WishForm(ModelForm):
    class Meta:
        model = Wish
        fields = ['bookName']


class SearchForm(ModelForm):
    class Meta:
        model = BookSearch
        fields = ['name']
