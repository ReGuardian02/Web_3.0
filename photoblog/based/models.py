from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, BooleanField


User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Название', unique=True, max_length=15)
    slug = models.SlugField('Слаг', unique=True, max_length=15)
    color = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор')
   
    image = models.ImageField(verbose_name='Картинка', blank=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self) -> str:
        return self.text
    
class Product(models.Model):
    title = models.TextField(max_length=50, verbose_name='Наименование товара')
    text = models.TextField(max_length=500, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='products', verbose_name='Автор')
   
    image = models.ImageField(verbose_name='Картинка', blank=True)
    tags = models.ForeignKey(Tag,
        related_name='tags',
        verbose_name='Теги',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self) -> str:
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
    )
    text = models.TextField('Текст',
                            help_text='Текст нового комментария')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self) -> str:
        return self.text[:15]

class Chat(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="chat",
        verbose_name="Сообщение",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="chats",
        verbose_name="Автор сообщения",
    )
    text = models.TextField('Текст',
                            help_text='Текст нового сообщения')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self) -> str:
        return self.text[:15]

class Feedback(models.Model):
    name = models.TextField(max_length=20, verbose_name='Имя')
    email = models.TextField(max_length=30, verbose_name='Адрес электронной почты')
    text = models.TextField(max_length=100, verbose_name='Текст отзыва')
