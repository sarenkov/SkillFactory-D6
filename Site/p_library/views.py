from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Book, Author, Publisher, Friend
from .forms import BookForm, AuthorForm, PublisherForm, ReaderForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'p_library/books.html'
    context_object_name = 'books'


class BookView(generic.DetailView):
    model = Book
    template_name = 'p_library/book.html'
    context_object_name = 'book'


class BookUpdate(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'p_library/update_form.html'


class BookCreate(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'p_library/update_form.html'


class BookDelete(generic.DeleteView):
    model = Book
    template_name = 'p_library/book_delete.html'
    success_url = reverse_lazy('p_library:books')


class AuthorsView(generic.ListView):
    model = Author
    template_name = 'p_library/authors.html'
    context_object_name = 'authors'


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'p_library/author.html'
    context_object_name = 'author'


class AuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'p_library/update_form.html'


class AuthorUpdate(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'p_library/update_form.html'


class AuthorDelete(generic.DeleteView):
    model = Author
    template_name = 'p_library/author_delete.html'
    success_url = reverse_lazy('p_library:authors')


class PublisherCreate(generic.CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'p_library/update_form.html'


class PublishersView(generic.ListView):
    model = Publisher
    template_name = 'p_library/publishers.html'
    context_object_name = 'publishers'


class PublisherView(generic.DetailView):
    model = Publisher
    template_name = 'p_library/publisher.html'
    context_object_name = 'publisher'


class PublisherUpdate(generic.UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'p_library/update_form.html'


class PublisherDelete(generic.DeleteView):
    model = Publisher
    template_name = 'p_library/publisher_delete.html'
    success_url = reverse_lazy('p_library:publishers')


class ReaderCreate(generic.CreateView):
    model = Friend
    form_class = ReaderForm
    template_name = 'p_library/update_form.html'


class ReadersView(generic.ListView):
    model = Friend
    template_name = 'p_library/readers.html'
    context_object_name = 'readers'


class ReaderView(generic.DetailView):
    model = Friend
    template_name = 'p_library/reader.html'
    context_object_name = 'reader'


class ReaderUpdate(generic.UpdateView):
    model = Friend
    template_name = 'p_library/update_form.html'
    form_class = ReaderForm


class ReaderDelete(generic.DeleteView):
    model = Friend
    template_name = 'p_library/reader_delete.html'
    success_url = reverse_lazy('p_library:readers')
