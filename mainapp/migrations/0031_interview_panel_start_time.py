# Generated by Django 4.1.1 on 2023-03-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0030_remove_candidate_rounds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview_panel',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]