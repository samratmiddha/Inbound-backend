# Generated by Django 4.1.1 on 2022-11-03 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_round_info_marks_obtained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asignee',
            field=models.ManyToManyField(blank=True, related_name='question_asignees', to=settings.AUTH_USER_MODEL),
        ),
    ]