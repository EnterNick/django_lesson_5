# Generated by Django 5.1.4 on 2024-12-05 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0003_remove_comments_author_alter_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 5, 13, 29, 1, 14403)),
        ),
    ]