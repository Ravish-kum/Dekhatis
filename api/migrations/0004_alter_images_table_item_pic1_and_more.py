# Generated by Django 4.1.5 on 2023-02-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cancellations_table_cancellations_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images_table',
            name='item_pic1',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic10',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic2',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic3',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic4',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic5',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic6',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic7',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic8',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='images_table',
            name='item_pic9',
            field=models.ImageField(default=None, upload_to='uploads/images'),
        ),
    ]
