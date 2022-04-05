# Generated by Django 4.0.3 on 2022-03-11 12:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(default='Anonymous', max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('edited_at', models.DateTimeField(default=datetime.datetime(2022, 3, 11, 15, 34, 26, 814028))),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'ordering': ('-created_at', '-edited_at', 'author'),
            },
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
