# Generated by Django 4.1 on 2022-08-28 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0023_remove_user_is_superuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='full_name',
        ),
    ]
