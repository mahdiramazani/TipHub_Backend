# Generated by Django 4.1 on 2022-08-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='static/assets/index.jpg', upload_to='user/image'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
