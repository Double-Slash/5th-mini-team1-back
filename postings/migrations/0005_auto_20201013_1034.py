# Generated by Django 3.1.1 on 2020-10-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0004_posting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='guide_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='project_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='qualifications',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='team_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='team_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
