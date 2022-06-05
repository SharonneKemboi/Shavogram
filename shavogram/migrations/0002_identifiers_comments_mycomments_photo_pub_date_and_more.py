# Generated by Django 4.0.5 on 2022-06-04 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shavogram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='identifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='mycomments',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='photo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=31, unique=True),
        ),
    ]
