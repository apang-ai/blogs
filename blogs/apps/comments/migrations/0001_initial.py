# Generated by Django 2.0.2 on 2020-07-06 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_content', models.CharField(max_length=1000, verbose_name='用户评论')),
                ('content_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
    ]