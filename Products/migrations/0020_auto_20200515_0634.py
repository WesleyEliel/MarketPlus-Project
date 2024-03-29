# Generated by Django 3.0.6 on 2020-05-15 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('Products', '0019_auto_20200509_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealoftheweek',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='dealoftheweek',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 5, 34, 7, 786083, tzinfo=utc)),
        ),
    ]
