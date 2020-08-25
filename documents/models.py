from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Document(models.Model):
    title = models.CharField('Название документа', max_length=50)
    file = models.FileField('Фаил',upload_to="document/")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

class Uslugi(models.Model):
    title = models.CharField('Наименование услуги', max_length=50)
    text = RichTextField('Описание услуги', blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    file = models.FileField('Фаил', blank=True, upload_to="document/")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
