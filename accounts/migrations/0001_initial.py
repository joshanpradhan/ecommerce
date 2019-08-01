# Generated by Django 2.2.3 on 2019-07-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]