# Generated by Django 4.1.5 on 2023-02-26 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adver_image', models.ImageField(upload_to='uploads/adver_images')),
                ('adver_url', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'advertisement_table',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='c_item_id',
            new_name='m_item_id',
        ),
        migrations.RemoveField(
            model_name='customer_table',
            name='customer_pass',
        ),
        migrations.AddField(
            model_name='customer_table',
            name='customer_cerdits_tokens',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer_table',
            name='customer_otp',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer_table',
            name='customer_state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='item_colour',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_finish',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_instructions',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='item_shipping_time',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_size',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_storage',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_visual_similarity',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='item_warrenty',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='query_table',
            name='bank_id',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='shop_table',
            name='manufacturer_address',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AddField(
            model_name='shop_table',
            name='manufacturer_name',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AddField(
            model_name='shop_table',
            name='manufacturer_phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shop_table',
            name='shop_brand_name',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='customer_table',
            name='customer_phone',
            field=models.CharField(default=None, max_length=14),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='shop_ordered',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='shop_table',
            name='shop_pass',
            field=models.CharField(default=None, max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Review_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=400)),
                ('events', models.ImageField(upload_to='uploads/reviews_images')),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.customer_table', verbose_name='customer')),
            ],
            options={
                'db_table': 'review_table',
            },
        ),
        migrations.CreateModel(
            name='Product_varient_table',
            fields=[
                ('item_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('v_item_id', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=50)),
                ('item_image', models.ImageField(upload_to='uploads/images')),
                ('item_categories', models.CharField(max_length=30)),
                ('item_detail', models.CharField(max_length=300)),
                ('item_cost', models.IntegerField()),
                ('item_revenue', models.IntegerField()),
                ('shop_pin', models.IntegerField()),
                ('item_size', models.CharField(max_length=30)),
                ('item_finish', models.CharField(max_length=30)),
                ('item_storage', models.CharField(max_length=30)),
                ('item_colour', models.CharField(max_length=30)),
                ('item_shipping_time', models.CharField(max_length=30)),
                ('item_warrenty', models.CharField(max_length=30)),
                ('item_instructions', models.CharField(max_length=30)),
                ('item_rating', models.IntegerField(default=0)),
                ('shop_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.shop_table', verbose_name='placer')),
            ],
            options={
                'db_table': 'product_varient_table',
            },
        ),
        migrations.CreateModel(
            name='Images_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_pic1', models.ImageField(upload_to='uploads/images')),
                ('item_pic2', models.ImageField(upload_to='uploads/images')),
                ('item_pic3', models.ImageField(upload_to='uploads/images')),
                ('item_pic4', models.ImageField(upload_to='uploads/images')),
                ('item_pic5', models.ImageField(upload_to='uploads/images')),
                ('item_pic6', models.ImageField(upload_to='uploads/images')),
                ('item_pic7', models.ImageField(upload_to='uploads/images')),
                ('item_pic8', models.ImageField(upload_to='uploads/images')),
                ('item_pic9', models.ImageField(upload_to='uploads/images')),
                ('item_pic10', models.ImageField(upload_to='uploads/images')),
                ('item_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.product', verbose_name='item')),
            ],
            options={
                'db_table': 'images_table',
            },
        ),
        migrations.CreateModel(
            name='Cancellations_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancellation_id', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(max_length=100)),
                ('transcation_id', models.CharField(max_length=200)),
                ('bank_id', models.CharField(max_length=200)),
                ('item_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.product', verbose_name='item')),
                ('placing_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.customer_table', verbose_name='customer')),
                ('shop_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.shop_table', verbose_name='shop')),
            ],
            options={
                'db_table': 'cancellations_table',
            },
        ),
    ]
