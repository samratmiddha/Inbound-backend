# Generated by Django 4.1.1 on 2023-03-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_remove_infotoconvey_round_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotoconvey',
            name='round_info',
            field=models.ForeignKey(blank=True, default=21, on_delete=django.db.models.deletion.CASCADE, to='mainapp.round_info'),
            preserve_default=False,
        ),
    ]
