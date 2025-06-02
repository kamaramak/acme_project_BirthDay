# birthday/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from .validators import real_age

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'
        ordering = ['tag']
        constraints = (
            models.UniqueConstraint(
                fields=('tag',),
                name='Unique tag',
            ),
        )

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        help_text='Необязательное поле',
        max_length=20,
        blank=True,
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,),
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True,
    )
    author = models.ForeignKey(
        User, verbose_name='Авто записи', on_delete=models.CASCADE, null=True
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов',
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'
        ordering = ['id']
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.first_name + self.last_name


class Congratulation(models.Model):
    text = models.TextField('Текст поздравдения')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulation',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('created_at',)
