# Generated by Django 3.2 on 2024-11-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]