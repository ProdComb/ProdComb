# Generated by Django 4.2.6 on 2023-10-19 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_product_unique_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='full_name',
        ),
    ]
