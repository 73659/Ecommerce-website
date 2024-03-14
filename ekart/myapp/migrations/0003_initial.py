# Generated by Django 5.0.2 on 2024-02-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField()),
                ('cat', models.IntegerField(verbose_name='Category')),
                ('product_details', models.CharField(max_length=500, verbose_name='Product Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
    ]
