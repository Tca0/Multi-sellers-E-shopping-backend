# Generated by Django 4.0.4 on 2022-05-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.CharField(max_length=255)),
                ('building_name', models.CharField(max_length=255)),
                ('building_number', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
    ]
