# Generated by Django 5.0.7 on 2024-10-10 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totem', '0005_curso_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='video',
        ),
    ]
