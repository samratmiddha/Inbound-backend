# Generated by Django 4.1.1 on 2022-09-10 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round_info',
            name='panel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.interview_panel'),
        ),
    ]
