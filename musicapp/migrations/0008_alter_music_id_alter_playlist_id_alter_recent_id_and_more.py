# Generated by Django 5.0.3 on 2024-04-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_music_alter_song_language_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Local', 'Local'), ('English', 'English')], default='Hindi', max_length=20),
        ),
    ]
