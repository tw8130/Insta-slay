# Generated by Django 3.0.6 on 2020-06-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0004_auto_20200603_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo_comments',
            field=models.CharField(max_length=150),
        ),
    ]
