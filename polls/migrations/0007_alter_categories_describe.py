# Generated by Django 4.0.2 on 2022-05-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_posts_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='describe',
            field=models.TextField(default='Da taFlair Django tutorials'),
        ),
    ]
