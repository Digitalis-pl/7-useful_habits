# Generated by Django 4.2.2 on 2024-08-06 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='associated_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('every_day', 'Ежедневно'), ('every_week', 'Еженедельно'), ('every_month', 'Ежемесячно')], default='every_day', help_text='Периодичность', max_length=100, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default='16:01'),
        ),
    ]
