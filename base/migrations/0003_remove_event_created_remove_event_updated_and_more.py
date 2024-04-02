# Generated by Django 5.0.1 on 2024-03-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/image/'),
        ),
    ]
