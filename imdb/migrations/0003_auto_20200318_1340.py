# Generated by Django 3.0.4 on 2020-03-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_auto_20200318_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='fb_likes',
            field=models.IntegerField(null=True),
        ),
    ]