from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {'title', 'description', 'detailed_description', 'date', 'status'}
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'detailed_description': 'Подробно',
            'date': 'Дата',
            'status': 'Статус'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title
