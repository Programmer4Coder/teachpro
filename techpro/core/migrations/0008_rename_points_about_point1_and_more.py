# Generated by Django 5.1.1 on 2024-12-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_blog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='points',
            new_name='point1',
        ),
        migrations.RenameField(
            model_name='why_choose_us',
            old_name='point',
            new_name='point1',
        ),
        migrations.AddField(
            model_name='about',
            name='point2',
            field=models.TextField(default='Default'),
        ),
        migrations.AddField(
            model_name='about',
            name='point3',
            field=models.TextField(default='Default'),
        ),
        migrations.AddField(
            model_name='why_choose_us',
            name='point2',
            field=models.TextField(default='Default'),
        ),
        migrations.AddField(
            model_name='why_choose_us',
            name='point3',
            field=models.TextField(default='Default'),
        ),
        migrations.AddField(
            model_name='why_choose_us',
            name='point4',
            field=models.TextField(default='Default'),
        ),
    ]