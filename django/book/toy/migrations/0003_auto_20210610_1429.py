# Generated by Django 3.2.2 on 2021-06-10 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0002_auto_20210610_0953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='emp',
            new_name='usr',
        ),
        migrations.AlterModelTable(
            name='usr',
            table='usr',
        ),
    ]
