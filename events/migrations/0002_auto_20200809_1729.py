# Generated by Django 3.0.3 on 2020-08-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsimages',
            old_name='image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='event',
            name='imageslist',
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='events.PostsImages'),
        ),
    ]