# Generated by Django 5.1.7 on 2025-03-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
