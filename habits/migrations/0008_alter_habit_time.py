# Generated by Django 4.2.2 on 2024-08-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default='34:28'),
        ),
    ]
