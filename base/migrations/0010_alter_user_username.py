# Generated by Django 4.1 on 2022-10-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
