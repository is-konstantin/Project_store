# Generated by Django 3.1.5 on 2021-03-21 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_bookincart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='cart.cart', verbose_name='Cart'),
        ),
    ]
