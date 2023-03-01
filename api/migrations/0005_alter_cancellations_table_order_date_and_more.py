# Generated by Django 4.1.5 on 2023-02-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_images_table_item_pic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancellations_table',
            name='order_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_otp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_state',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic1',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic10',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic2',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic3',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic4',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic5',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic6',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic7',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic8',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic9',
            field=models.ImageField(blank=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_colour',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_finish',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_instructions',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_shipping_time',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_storage',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_visual_similarity',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_warrenty',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_item_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='query_table',
            name='bank_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='manufacturer_address',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='manufacturer_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='shop_brand_name',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='shop_ordered',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='shop_pass',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Product_varient_table',
        ),
    ]
