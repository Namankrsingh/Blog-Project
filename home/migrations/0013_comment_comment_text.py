# Generated by Django 5.1.7 on 2025-03-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_user_blog_user_id_rename_user_comment_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default=''),
        ),
    ]
