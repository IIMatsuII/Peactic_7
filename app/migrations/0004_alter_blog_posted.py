# Generated by Django 5.0.4 on 2024-04-23 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 4, 23, 22, 35, 4, 175272), verbose_name='Опубликована'),
        ),
    ]
