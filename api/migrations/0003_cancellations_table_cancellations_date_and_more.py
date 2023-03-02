# Generated by Django 4.1.5 on 2023-02-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advertisement_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancellations_table',
            name='cancellations_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cancellations_table',
            name='order_date',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='product_varient_table',
            name='item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.product', verbose_name='item'),
        ),
        migrations.AlterField(
            model_name='product_varient_table',
            name='v_item_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]