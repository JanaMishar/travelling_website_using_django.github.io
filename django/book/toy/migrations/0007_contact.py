# Generated by Django 3.2.2 on 2021-06-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0006_auto_20210624_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('sem', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
