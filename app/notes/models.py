from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from pytils.translit import slugify


class Notes(models.Model):
    """Заметки"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    text_note = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Текст заметки')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user_key = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    # ссылка на текущий объект для шаблона
    def get_absolute_url(self):
        return reverse('view', kwargs={'note_slug': self.slug})

    # добавление слага из формы
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['id']
