# Generated by Django 4.1 on 2022-08-18 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0016_user_is_teacher'),
        ('Tutorial_app', '0014_videotutorial_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotutorial',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_tutorial', to='Acount_app.techer', unique=True),
        ),
    ]
