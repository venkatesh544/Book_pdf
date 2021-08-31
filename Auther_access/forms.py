from django import forms

from Auther_access.models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model =Book
        fields =('title','author','pdf')
