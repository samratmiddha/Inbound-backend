# Generated by Django 4.1.1 on 2022-11-04 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_question_asignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotoconvey',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.season'),
            preserve_default=False,
        ),
    ]