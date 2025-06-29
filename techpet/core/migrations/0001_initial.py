# Generated by Django 5.1.7 on 2025-06-26 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
            ],
        ),
        migrations.CreateModel(
            name='PetGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PetData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.petgender')),
            ],
        ),
    ]
