# Generated by Django 5.0.3 on 2024-04-25 12:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_artist_id_alter_profile_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='UserProfiler',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
