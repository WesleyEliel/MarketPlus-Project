# Generated by Django 3.0.3 on 2020-04-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0013_auto_20200413_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
