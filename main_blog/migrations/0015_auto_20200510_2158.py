# Generated by Django 2.2.10 on 2020-05-10 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0014_auto_20200510_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category_url',
        ),
    ]
