# Generated by Django 3.2.8 on 2021-11-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0016_alter_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('started', 'STARTED'), ('late_submitted', 'LATE SUBMITTED'), ('completed', 'COMPLETED')], default='started', max_length=64),
        ),
    ]
