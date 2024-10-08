from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from slugify import slugify


User = get_user_model()


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Информация о книге")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Опубликовано", editable=False)
    file = models.FileField(upload_to='books/file/', blank=False, verbose_name="Файл (текст книги)")
    image = models.ImageField(upload_to='books/image/', blank=True, verbose_name="Изображение (обложка)")
    slug = models.SlugField(max_length=200, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
