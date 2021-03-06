# Generated by Django 4.0.3 on 2022-03-11 12:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0))),
            ],
            options={
                'ordering': ('-created_at', '-updated_at', 'title', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('author', models.CharField(default='Anonymous', max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('edited_at', models.DateTimeField(default=datetime.datetime(2022, 3, 11, 15, 23, 20, 578151))),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'ordering': ('-created_at', '-edited_at', 'author'),
            },
        ),
    ]
