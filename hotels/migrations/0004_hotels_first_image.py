# Generated by Django 4.2.1 on 2024-05-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_remove_hotels_first_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='first_image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
