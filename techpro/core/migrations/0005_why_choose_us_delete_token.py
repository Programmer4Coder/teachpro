# Generated by Django 5.1.1 on 2024-12-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why_choose_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('point', models.TextField(default='Default')),
                ('image', models.ImageField(upload_to='token/')),
            ],
        ),
        migrations.DeleteModel(
            name='token',
        ),
    ]
