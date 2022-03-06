from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import range_year_validate

User = get_user_model()


class Categorie(models.Model):
    name = models.TextField('Название категории', max_length=256)
    slug = models.SlugField(
        'Адрес категории',
        unique=True,
        max_length=50,)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField('Название жанра', max_length=256)
    slug = models.SlugField(
        'Адрес жанра',
        unique=True,
        max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField('Название произведения', max_length=200)
    description = models.TextField('Описание произведения', blank=True)
    year = models.IntegerField(
        'Год издания произведения',
        blank=True,
        null=False,
        validators=[range_year_validate, ])
    category = models.ForeignKey(
        Categorie, on_delete=models.SET_NULL,
        related_name='c_titles',
        blank=False, null=True,
        verbose_name='Категория', help_text='Выберите категорию произведения',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='g_titles',
        verbose_name='Жанры',)

    def __str__(self):
        return self.name[:100]


class Review(models.Model):
    text = models.TextField('Текст ревью', max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', verbose_name='Автор',)
    score = models.SmallIntegerField(
        'Оценка', validators=[MaxValueValidator(10), MinValueValidator(0)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews', verbose_name='Произведение',)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique_review'),
        ]

    def __str__(self):
        return self.text[:100]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Автор')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Отзыв')
    text = models.TextField('Текст комментария', max_length=200)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
