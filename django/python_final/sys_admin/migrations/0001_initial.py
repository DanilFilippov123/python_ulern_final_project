# Generated by Django 5.0.1 on 2024-01-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableGraphicPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('graphic_title', models.CharField(max_length=150)),
                ('graphic', models.ImageField(upload_to='graphics/')),
                ('table_title', models.CharField(max_length=150)),
                ('table', models.FileField(upload_to='tables/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('graphics_and_tables', models.ManyToManyField(to='sys_admin.tablegraphicpair')),
            ],
        ),
    ]
