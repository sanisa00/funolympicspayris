# Generated by Django 5.0.1 on 2024-03-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_event_video_url_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='media/events_videos/'),
        ),
    ]