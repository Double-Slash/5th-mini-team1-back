# Generated by Django 3.1.1 on 2020-10-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]