# Generated by Django 5.0.1 on 2024-03-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_contact_number_user_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sports_category',
            field=models.CharField(choices=[('ATHLETICS', 'Athletics'), ('AQUATICS', 'Aquatics'), ('COMBAT', 'Combat'), ('GYMNASTICS', 'Gymnastics'), ('SHOOTING', 'Shooting'), ('TEAM', 'Team')], max_length=20, null=True),
        ),
    ]