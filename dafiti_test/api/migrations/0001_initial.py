# Generated by Django 3.1.7 on 2021-02-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='product', max_length=100)),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=10)),
                ('img_src', models.TextField(db_column='photo_src', max_length=300)),
            ],
        ),
    ]
