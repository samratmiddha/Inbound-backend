# Generated by Django 4.1.1 on 2022-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_interview_panel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview_panel',
            name='custom_questions',
        ),
        migrations.RemoveField(
            model_name='round',
            name='dates',
        ),
        migrations.AddField(
            model_name='interview_panel',
            name='type',
            field=models.CharField(choices=[('tech', 'Tech'), ('hr', 'HR')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]