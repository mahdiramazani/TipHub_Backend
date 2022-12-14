# Generated by Django 4.1 on 2022-09-15 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0033_alter_techer_options_alter_user_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tutorial_app', '0021_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها'},
        ),
        migrations.AlterModelOptions(
            name='videotutorial',
            options={'ordering': ('-created',), 'verbose_name': 'ویدیو', 'verbose_name_plural': 'ویدیوها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='متن کامنت'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replay', to='Tutorial_app.comment', verbose_name='کامنت مرجع'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Tutorial_app.videotutorial', verbose_name='ویدیو'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(related_name='subcategory', to='Tutorial_app.category', verbose_name='نام دسته بندی مرجع'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=30, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام تگ'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='category',
            field=models.ManyToManyField(related_name='videotutorial', to='Tutorial_app.subcategory', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='discription',
            field=models.TextField(verbose_name='توضیحات ویدیو'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='ویدیو فعال هست یا خیر؟'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='special_video',
            field=models.BooleanField(verbose_name='مخصوص اعضای ویژه؟'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='tag',
            field=models.ManyToManyField(related_name='videotutorial', to='Tutorial_app.tags', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_tutorial', to='Acount_app.techer', verbose_name='مدرس'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='titel',
            field=models.CharField(max_length=100, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='video',
            field=models.FileField(upload_to='videototorial/video', verbose_name='ویدیو'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='video_cover',
            field=models.FileField(upload_to='videotutorial/iamge', verbose_name='کاور ویدیو'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='video_time',
            field=models.CharField(max_length=50, verbose_name='ویدیو'),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='view',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
