# Generated by Django 4.0 on 2022-01-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_merge_20220124_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]