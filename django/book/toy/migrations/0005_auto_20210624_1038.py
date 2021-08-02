# Generated by Django 3.2.2 on 2021-06-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0004_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='usrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'usrs',
            },
        ),
        migrations.DeleteModel(
            name='tour',
        ),
    ]