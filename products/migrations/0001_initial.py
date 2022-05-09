# Generated by Django 4.0.4 on 2022-05-09 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='categories.category')),
            ],
        ),
    ]
