# Generated by Django 3.0.3 on 2020-03-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_productanonymousreview_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=5, verbose_name='Your Rating'),
        ),
    ]
