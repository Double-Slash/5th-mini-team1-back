# Generated by Django 3.1.1 on 2020-10-14 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('host_info', models.CharField(max_length=100, null=True)),
                ('award', models.CharField(max_length=100, null=True)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('location', models.TextField(null=True)),
                ('team_name', models.CharField(max_length=100, null=True)),
                ('team_description', models.TextField(null=True)),
                ('project_description', models.TextField(null=True)),
                ('guide_text', models.TextField(null=True)),
                ('qualifications', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='postings', to=settings.AUTH_USER_MODEL)),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Postings', to='postings.postingtype')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='postings', to='hashtags.DefaultTag')),
            ],
        ),
    ]
