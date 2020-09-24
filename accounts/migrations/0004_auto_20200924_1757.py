# Generated by Django 3.1.1 on 2020-09-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_usermanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserManager',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
