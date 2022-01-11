# Generated by Django 4.0 on 2021-12-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerstalk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('flowers', 'Flowers'), ('gifts', 'Gifts')], default='flowers', max_length=10)),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ('-created',),
            },
        ),
        migrations.DeleteModel(
            name='Flowers',
        ),
    ]
