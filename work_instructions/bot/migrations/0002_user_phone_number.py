# Generated by Django 3.2.8 on 2021-11-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default=0, max_length=9),
        ),
    ]
