# Generated by Django 5.0.1 on 2024-01-18 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0005_tablegraphicpair_html_table_alter_article_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablegraphicpair',
            name='html_table',
        ),
    ]
