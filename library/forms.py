from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super(BookForm, self).__init__(*args, **kwargs)
        if author:
            self.fields['author'].initial = author
            self.fields['author'].disabled = True

    class Meta:
        model = Book
        fields = ['author', 'title', 'text', 'file', 'image']
