# Generated by Django 4.0.5 on 2022-06-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shavogram', '0002_identifiers_comments_mycomments_photo_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Welcome', max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]