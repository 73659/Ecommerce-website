# Generated by Django 5.0.2 on 2024-03-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_img',
            field=models.ImageField(null='True', upload_to='image'),
            preserve_default='True',
        ),
    ]
