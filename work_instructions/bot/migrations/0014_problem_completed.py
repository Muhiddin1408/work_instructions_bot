# Generated by Django 3.2.8 on 2021-11-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_alter_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='completed',
            field=models.CharField(choices=[('completed', 'COMPLETED'), ('not_completed', 'NOT COMPLETED')], default='completed', max_length=64),
        ),
    ]
