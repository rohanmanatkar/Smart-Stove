# Generated by Django 2.2.2 on 2019-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('proximity1', models.FloatField()),
                ('proximity2', models.FloatField()),
            ],
        ),
    ]
