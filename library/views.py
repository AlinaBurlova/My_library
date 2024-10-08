from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book


def root(request):
    return render(request, template_name='library/index.html')


def index(request):
    return render(request, template_name='library/index.html')


def about(request):
    context = {
        'name': 'Алина',
        'lastname': 'Бурлова',
        'email': 'alina-burlova@mail.ru',
        'title': "О сайте"
    }
    return render(request, template_name='library/about.html', context=context)


@login_required
def add_book(request):
    if request.method == "GET":
        form = BookForm(author=request.user)
        context = {
            'form': form,
            'title': "Добавление книги",
        }
        return render(request, template_name='library/add_book.html', context=context)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            book = Book()
            book.author = form.cleaned_data['author']
            book.title = form.cleaned_data['title']
            book.text = form.cleaned_data['text']
            book.file = form.cleaned_data['file']
            book.image = form.cleaned_data['image']
            book.save()
        return index(request)


def book_list(request):
    books = Book.objects.all()
    context = {
        'title': "Книги",
        'posts': books,
    }
    return render(request, template_name='library/books.html', context=context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'title': "Информация о книге",
        'book': book,
    }
    return render(request, template_name='library/book_detail.html', context=context)


@login_required
def book_edit(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book, author=request.user)
        if form.is_valid():
            form.save()

            return book_list(request)
    else:
        form = BookForm(instance=book, author=request.user)
    context = {
            'form': form,
            'title': "Редактировать характеристики книги",
    }
    return render(request, template_name='library/book_edit.html', context=context)


@login_required
def book_delete(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        book.delete()
        return redirect("library:book_list")
    return render(request, template_name="library/book_delete.html", context={"book": book})


def forbidden(request, exception):
    return render(request, "library/403.html", status=403)


def page_not_found(request, exception):
    return render(request, "library/404.html", status=404)


def server_error(request):
    return render(request, "library/500.html", status=500)