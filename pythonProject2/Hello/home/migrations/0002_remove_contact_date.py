# Generated by Django 4.2.5 on 2023-09-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
