# Generated by Django 4.2.2 on 2024-08-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_options_alter_habit_associated_habit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='prize',
            field=models.CharField(blank=True, help_text='Награда за соблюдение', max_length=250, null=True, verbose_name='Награда'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default='17:31'),
        ),
    ]
