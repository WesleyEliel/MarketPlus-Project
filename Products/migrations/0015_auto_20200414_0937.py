# Generated by Django 3.0.3 on 2020-04-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_productcategory_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_in_stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
