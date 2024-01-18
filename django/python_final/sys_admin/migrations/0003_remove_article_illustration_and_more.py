# Generated by Django 5.0.1 on 2024-01-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0002_article_illustration_article_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='illustration',
        ),
        migrations.AlterField(
            model_name='article',
            name='graphics_and_tables',
            field=models.ManyToManyField(blank=True, null=True, to='sys_admin.tablegraphicpair'),
        ),
    ]
