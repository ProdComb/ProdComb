# Generated by Django 4.2.6 on 2023-10-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_combination_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='combination',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unusable'), (1, 'Usable but has significant issues)'), (2, 'Works good but has some minor issues'), (3, 'Works perfectly with no issues')], default=2),
            preserve_default=False,
        ),
    ]