from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class afisha(models.Model):
    title = models.CharField('Название мероприятия', max_length=50)
    description = RichTextField('Текст записи', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date_in = models.DateField('Дата начала показа')
    date_out = models.DateField('Дата окочания показа')
    time = models.CharField('Время показа', max_length=20)
    price = models.IntegerField()
    date_pub = models.DateField(auto_now_add=True)



    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиша"

class holiday(models.Model):
    title = models.CharField('Название праздника', max_length=50)
    description = RichTextField('Описание праздника', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date_h = models.DateField('Дата')
    date_pub = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"