# Generated by Django 5.1.1 on 2024-10-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_total_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total_quantity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('drugs', 'Drugs'), ('cosmetics', 'Cosmetics'), ('food', 'Food'), ('clothing', 'Flothing')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
