from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
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

class Feedback(models.Model):
    name = models.TextField(max_length=20, verbose_name='Имя')
    email = models.TextField(max_length=30, verbose_name='Адрес электронной почты')
    text = models.TextField(max_length=100, verbose_name='Текст отзыва')