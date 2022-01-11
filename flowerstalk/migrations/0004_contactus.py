# Generated by Django 4.0 on 2021-12-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerstalk', '0003_items_image_alter_items_price_alter_items_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=200)),
                ('telephone', models.CharField(max_length=32)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
