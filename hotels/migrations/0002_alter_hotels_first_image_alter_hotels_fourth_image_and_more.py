# Generated by Django 4.2.1 on 2024-05-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='first_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='fourth_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='second_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='third_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
