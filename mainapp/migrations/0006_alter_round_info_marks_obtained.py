# Generated by Django 4.1.1 on 2022-10-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_question_status_normalized_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round_info',
            name='marks_obtained',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
