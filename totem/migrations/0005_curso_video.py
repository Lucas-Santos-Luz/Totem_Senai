# Generated by Django 5.0.7 on 2024-10-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totem', '0004_remove_curso_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
