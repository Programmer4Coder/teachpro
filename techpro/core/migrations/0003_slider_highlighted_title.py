# Generated by Django 5.1.1 on 2024-12-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_token_rename_contactinfo_contact_alter_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='highlighted_title',
            field=models.CharField(default='Default', max_length=100),
        ),
    ]
