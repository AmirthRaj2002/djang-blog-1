# Generated by Django 4.0.3 on 2022-03-15 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comment_edited_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 1, 48, 44, 387694)),
        ),
    ]
