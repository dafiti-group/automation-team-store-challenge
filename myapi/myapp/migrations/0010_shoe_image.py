# Generated by Django 3.1.5 on 2021-02-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210208_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=models.ImageField(default='src/img/default.png', upload_to=''),
        ),
    ]
