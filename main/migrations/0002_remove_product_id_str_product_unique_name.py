# Generated by Django 4.2.6 on 2023-10-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id_str',
        ),
        migrations.AddField(
            model_name='product',
            name='unique_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
