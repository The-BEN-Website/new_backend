# Generated by Django 4.2 on 2024-02-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_message_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique_for_date='date'),
        ),
    ]
