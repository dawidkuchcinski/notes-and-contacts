# Generated by Django 2.0.13 on 2019-03-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190323_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='priority',
            field=models.IntegerField(null=True),
        ),
    ]
