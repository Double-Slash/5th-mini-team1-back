# Generated by Django 3.1.1 on 2020-10-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0004_posting_image'),
        ('accounts', '0013_auto_20201013_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='written_posts',
            field=models.ManyToManyField(blank=True, to='postings.Posting'),
        ),
    ]
