# Generated by Django 4.1.1 on 2022-11-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_sectional_marks_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_status',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
