# Generated by Django 2.0.13 on 2019-04-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190417_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['email_subject', 'email_address']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['item_type', 'item_model']},
        ),
    ]
