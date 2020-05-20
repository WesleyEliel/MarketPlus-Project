# Generated by Django 3.0.6 on 2020-05-16 16:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('location_point', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('date_of_birth', models.DateField(help_text='Enter your Birthday following this format YYYY/MM/DD')),
                ('profession', models.CharField(help_text='Help us to provide you analytics Articles', max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=40)),
                ('phone', models.CharField(max_length=25)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('city_town', models.CharField(blank=True, max_length=30)),
                ('other_note', models.CharField(blank=True, max_length=220, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='a_user_first_address', to='Accounts.Address')),
                ('another_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='a_user_other_address', to='Accounts.Address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]