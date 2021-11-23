# Generated by Django 3.2.9 on 2021-11-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bordaapp', '0002_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='allowed_users',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='options',
            field=models.TextField(),
        ),
    ]
