# Generated by Django 4.0.2 on 2022-02-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorml', '0009_article_script'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='script',
            field=models.TextField(null=True, verbose_name='Скрипт'),
        ),
    ]