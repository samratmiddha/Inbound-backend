# Generated by Django 4.1.1 on 2023-02-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_sectional_marks_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='round_info',
            name='normalized_marks',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
