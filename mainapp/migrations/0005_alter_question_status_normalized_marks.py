# Generated by Django 4.1.1 on 2022-09-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_question_status_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_status',
            name='normalized_marks',
            field=models.FloatField(blank=True, default=models.IntegerField(blank=True, default=0, null=True)),
        ),
    ]