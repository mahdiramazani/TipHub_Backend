# Generated by Django 4.1 on 2022-08-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial_app', '0006_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotutorial',
            name='category',
            field=models.ManyToManyField(related_name='videotutorial', to='Tutorial_app.subcategory'),
        ),
    ]
