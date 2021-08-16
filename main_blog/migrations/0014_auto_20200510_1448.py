# Generated by Django 2.2.10 on 2020-05-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0013_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_name',
            field=models.CharField(default=999, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category_url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]