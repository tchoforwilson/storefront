# Generated by Django 5.1 on 2024-08-24 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                          INSERT INTO store_collection(title)
                          VALUES('Collection1')
                          """, """
                          DELETE FROM store_collection
                          WHERE title='Collection1'
                          """)
    ]
