# Generated by Django 2.2 on 2020-07-25 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200725_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecolumn',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
    ]