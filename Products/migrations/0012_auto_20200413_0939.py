# Generated by Django 3.0.3 on 2020-04-13 08:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_auto_20200404_1922'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('is_active', django.db.models.manager.Manager()),
            ],
        ),
    ]
