from django.db import models
from django.utils import timezone
from django.db.models import TextChoices

# Create your models here.


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Неактивна'


class Task(models.Model):
    date = models.CharField(max_length=50, null=True, blank=True, verbose_name="Дата")
    status = models.CharField(verbose_name="Статус", choices=StatusChoice.choices, max_length=20, default=StatusChoice.ACTIVE)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    detailed_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Детально")
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")
    deleted_at = models.DateTimeField(verbose_name="Время и дата удаления", null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.description}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задание'


