# Generated by Django 2.0.13 on 2019-03-23 15:19

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_shortcut', models.CharField(max_length=50)),
                ('branch_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('branch_email_address', models.EmailField(max_length=254)),
                ('branch_city', models.CharField(max_length=50)),
                ('branch_street', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email_address', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Branch')),
            ],
        ),
    ]
