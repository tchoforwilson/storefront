# Generated by Django 5.1 on 2024-08-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_last_updated_product_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Collection',
            new_name='collection',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
