# Generated by Django 4.0.3 on 2022-04-30 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='address',
        ),
    ]
