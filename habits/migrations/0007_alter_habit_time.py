# Generated by Django 4.2.2 on 2024-08-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_habit_next_day_to_do_alter_habit_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default='21:59'),
        ),
    ]
