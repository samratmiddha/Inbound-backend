# Generated by Django 4.1.1 on 2022-09-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_candidate_rounds_alter_candidate_season_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='enrolment_number',
            field=models.CharField(default=21117109, max_length=8, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
