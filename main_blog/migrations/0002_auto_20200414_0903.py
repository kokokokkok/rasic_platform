# Generated by Django 2.2.10 on 2020-04-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
    ]