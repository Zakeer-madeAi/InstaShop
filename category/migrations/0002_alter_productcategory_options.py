# Generated by Django 5.0 on 2023-12-17 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['-created_at'], 'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
    ]