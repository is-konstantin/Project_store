# Generated by Django 3.1.5 on 2021-03-22 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210321_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='cart.cart', verbose_name='Cart'),
        ),
    ]
