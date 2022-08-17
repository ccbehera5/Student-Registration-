# Generated by Django 3.0 on 2022-06-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Mobaile', models.BigIntegerField()),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
    ]
