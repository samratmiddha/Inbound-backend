# Generated by Django 4.1.1 on 2023-03-11 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_chats_panel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotoconvey',
            name='round_info',
        ),
    ]
