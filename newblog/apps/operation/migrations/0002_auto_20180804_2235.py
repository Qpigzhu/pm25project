# Generated by Django 2.1 on 2018-08-04 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
        ('blog', '0002_auto_20180804_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='点赞的用户'),
        ),
        migrations.AddField(
            model_name='hous',
            name='fav_blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='hous',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]