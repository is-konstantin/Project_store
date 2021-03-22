# Generated by Django 3.1.5 on 2021-03-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_picture',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_changes',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_entry',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
