# Generated by Django 3.0.3 on 2020-08-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_a',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
