# Generated by Django 3.0.7 on 2020-07-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='leadership',
            field=models.BooleanField(),
        ),
    ]
