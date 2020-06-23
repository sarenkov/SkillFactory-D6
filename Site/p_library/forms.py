from django import forms
from .models import Book, Author, Publisher, Friend


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Publisher
        fields = '__all__'


class ReaderForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'
