# Generated by Django 3.2.8 on 2021-11-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_alter_task_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.CharField(blank='completed', choices=[('completed', 'COMPLETED'), ('not_completed', 'NOT COMPLETED')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]