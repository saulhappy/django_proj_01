# Generated by Django 4.0.2 on 2022-03-05 17:10

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorages, upload_to='products/'),
        ),
    ]
