# Generated by Django 4.1.1 on 2023-02-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_infotoconvey_round_info_alter_round_info_panel'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectional_marks',
            name='normalized_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='session',
            field=models.IntegerField(default=2023),
        ),
    ]