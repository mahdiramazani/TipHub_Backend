# Generated by Django 4.1 on 2022-08-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0009_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(default=1, upload_to='user/image'),
            preserve_default=False,
        ),
    ]
