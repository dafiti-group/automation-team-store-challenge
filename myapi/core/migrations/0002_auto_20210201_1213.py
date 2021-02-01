# Generated by Django 3.1.5 on 2021-02-01 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='color',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='style',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='type',
        ),
        migrations.RemoveField(
            model_name='shoeinstance',
            name='shoe',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
        migrations.DeleteModel(
            name='ShoeInstance',
        ),
        migrations.DeleteModel(
            name='Style',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
